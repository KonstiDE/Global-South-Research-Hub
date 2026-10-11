# Global-South-Research-Hub
:earth_africa: Welcome to the Global South Research Hub :satellite:

The purpose of this repository is to notify researchers with a focus of topics in the context of the Global South about datasets, publications and connect people.

Furthermore, frequently used script to download datasets can be found here.

Please feel free to stick around and subscribe to the bi-monthly mailing newsletter <a src="" auto="_blank">here</a>.

<hr>

### Publicly available datasets
# Earth Observation & Global South Research Datasets

This repository contains a curated collection of datasets and their respective download scripts used for our research, with a strong focus on settlement development, population mapping, and Earth Observation in the Global South.

| Dataset | Link | Script to download | 
|---------|------|--------------------| 
| <td colspan=3><b>Settlement Development</b></td> | | |
| World Settlement Footprint (WSF) 2015 | [EOC Geoservice](https://geoservice.dlr.de/web/maps/eoc:wsf2015) | [download_wsf2015.py](scripts/download_wsf2015.py) | 
| World Settlement Footprint (WSF) 2019 | [EOC Geoservice](https://geoservice.dlr.de/web/maps/eoc:wsf2019) | [download_wsf2019.py](scripts/download_wsf2019.py) | 
| WSF Evolution (1985-2015) | [EOC Geoservice](https://geoservice.dlr.de/web/maps/eoc:wsf_evolution) | [download_wsf_evolution.py](scripts/download_wsf_evolution.py) | 
| WSF 3D (Building Volume/Height) | [EOC Geoservice](https://geoservice.dlr.de/web/maps/eoc:wsf3d) | [download_wsf3d.py](scripts/download_wsf3d.py) | 
| Global Human Settlement Layer (GHSL) Built-up | [JRC GHSL](https://ghsl.jrc.ec.europa.eu/ghs_bu.php) | [download_ghs_built.sh](scripts/download_ghs_built.sh) | 
| GHS-SMOD (Settlement Model) | [JRC GHSL](https://ghsl.jrc.ec.europa.eu/ghs_smod.php) | [download_ghs_smod.sh](scripts/download_ghs_smod.sh) | 
| <td colspan=3><b>Embedding Spaces & Foundation Models</b></td> | | |
| AlphaEarth Embeddings | *Internal/Requires Access* | [fetch_alphaearth_embeds.py](scripts/fetch_alphaearth_embeds.py) | 
| Tessera Embeddings | *Internal/Requires Access* | [fetch_tessera_embeds.py](scripts/fetch_tessera_embeds.py) | 
| Satlas (Super-Resolution/Embeddings) | [Satlas AllenAI](https://satlas.allenai.org/) | [download_satlas.py](scripts/download_satlas.py) | 
| Prithvi (NASA/IBM Geospatial FM) | [Hugging Face](https://huggingface.co/ibm-nasa-geospatial) | [download_prithvi.py](scripts/download_prithvi.py) | 
| <td colspan=3><b>Land Cover Classifications</b></td> | | |
| ESA WorldCover 10m | [ESA WorldCover](https://esa-worldcover.org/en) | [download_worldcover.py](scripts/download_worldcover.py) | 
| Google Dynamic World | [Dynamic World](https://dynamicworld.app/) | [download_dynamic_world.py](scripts/download_dynamic_world.py) | 
| <td colspan=3><b>Buildings & Infrastructure</b></td> | | |
| Google Open Buildings (Africa/Asia/LatAm) | [Google Research](https://sites.research.google/open-buildings/) | [download_open_buildings.py](scripts/download_open_buildings.py) | 
| Microsoft Global Building Footprints | [GitHub / Planetary Computer](https://github.com/microsoft/GlobalMLBuildingFootprints) | [download_ms_buildings.py](scripts/download_ms_buildings.py) | 
| GRID3 (Geo-Referenced Infrastructure) | [GRID3 Data Hub](https://grid3.org/data) | [download_grid3_pois.py](scripts/download_grid3_pois.py) | 
| <td colspan=3><b>Population & Demographics</b></td> | | |
| WorldPop (Unconstrained & Constrained) | [WorldPop Data](https://www.worldpop.org/) | [download_worldpop.py](scripts/download_worldpop.py) | 
| GHS-POP (Population Grid) | [JRC GHSL](https://ghsl.jrc.ec.europa.eu/ghs_pop.php) | [download_ghs_pop.sh](scripts/download_ghs_pop.sh) | 
| Meta HRSL (High-Resolution Settlement) | [CIESIN / Meta](https://ciesin.columbia.edu/data/hrsl/) | [download_meta_hrsl.py](scripts/download_meta_hrsl.py) | 
| <td colspan=3><b>Nighttime Lights & Socio-economic</b></td> | | |
| VIIRS Nighttime Lights (VNP46A1/A2) | [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) | [download_viirs_ntl.py](scripts/download_viirs_ntl.py) | 






