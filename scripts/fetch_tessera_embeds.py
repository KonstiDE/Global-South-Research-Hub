import argparse
import subprocess
from pathlib import Path
import geopandas as gpd
import rasterio
from rasterio.warp import transform_bounds


def get_tessera(input_path: Path, expand_factor: float = 1):
    ext = input_path.suffix.lower()

    if ext == ".tif" or ext == ".tiff":
        with rasterio.open(input_path) as src:
            bounds = src.bounds  # (left, bottom, right, top)
            src_crs = src.crs

            # Reproject bounds to WGS84 (EPSG:4326) if not already
            if src_crs != "EPSG:4326":
                minx, miny, maxx, maxy = transform_bounds(
                    src_crs, "EPSG:4326", bounds.left, bounds.bottom, bounds.right, bounds.top
                )
            else:
                minx, miny, maxx, maxy = bounds.left, bounds.bottom, bounds.right, bounds.top

    elif ext == ".gpkg" or ext == ".shp":
        gdf = gpd.read_file(input_path)

        # Reproject to WGS84 if needed
        if gdf.crs != "EPSG:4326":
            gdf = gdf.to_crs("EPSG:4326")

        minx, miny, maxx, maxy = gdf.total_bounds

    else:
        raise ValueError(f"Unsupported file format: {ext}. Use .tif or .gpkg.")

    if expand_factor != 1:
        # Calculate center and dimensions
        center_lon = (minx + maxx) / 2.0
        center_lat = (miny + maxy) / 2.0
        half_width = ((maxx - minx) / 2.0) * expand_factor
        half_height = ((maxy - miny) / 2.0) * expand_factor

        # Apply expansion
        new_minx = center_lon - half_width
        new_miny = center_lat - half_height
        new_maxx = center_lon + half_width
        new_maxy = center_lat + half_height

        return f"{new_minx:.4f},{new_miny:.4f},{new_maxx:.4f},{new_maxy:.4f}"
    else:
        return f"{minx:.4f},{miny:.4f},{maxx:.4f},{maxy:.4f}"


def main():
    parser = argparse.ArgumentParser(description="Download geotessera data from a spatial file (.tif or .gpkg).")
    parser.add_argument("input", type=Path, help="Path to input .tif or .gpkg file")
    parser.add_argument("--year", type=int, default=2023, help="Year to download (default: 2023)")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output directory (defaults to a folder next to the input file)",
    )
    parser.add_argument(
        "--expand",
        type=float,
        default=1.0,
        help="Factor to expand the bounding box (default:s to 1.0 => no expansion)",
    )

    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: Input file {args.input} does not exist.")
        return

    # Determine output path
    if args.output is None:
        output_dir = args.input.parent
    else:
        output_dir = args.input.parent / args.output

    # Get the bounding box string
    bbox_str = get_tessera(args.input, expand_factor=args.expand)
    print(f"Computed BBox (expanded {args.expand}x): {bbox_str}")

    # Build and run the geotessera command
    cmd = [
        "geotessera",
        "download",
        "--bbox",
        bbox_str,
        "--year",
        str(args.year),
        "--output",
        str(output_dir),
    ]

    print(f"Running command: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
    print(f"Successfully downloaded data to: {output_dir}")


if __name__ == "__main__":
    main()

    # Alternatively uncomment the following section if executin from python
    get_tessera(input_path="your input file", expand_factor=1.0)