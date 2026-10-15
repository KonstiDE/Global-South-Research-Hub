# Earth Observation & Global South Research Datasets

This repository contains a curated collection of datasets and their respective download scripts used for our research, with a strong focus on settlement development, population mapping, and Earth Observation in the Global South.

<hr>

So far, the newsletter consists of a summary of a ***Google Scholar Alert*** with various tags. The tags can be edited by anyone that receives the newsletter.

If you want to receive the newsletter, please visit [https://www.listserv.dfn.de/eo-global-south](https://www.listserv.dfn.de/eo-global-south).

Current tags of the scholar notifications:
```text
global south, informal, settlement, urban, development, sustainable, biomass, mining, 
```

| Dataset                                       | Link                                                                                   | Script to download                                              | 
|-----------------------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------| 
|                                               |                                                                                        |                                                                 |
|                                               |                                                                                        |                                                                 |
| **SETTLEMENT DEVELOPMENT**                    |                                                                                        |                                                                 | 
| World Settlement Footprint (WSF) 2015         | [EOC Geoservice](https://geoservice.dlr.de/web/maps/eoc:wsf2015)                       | [download_wsf2015.py](scripts/download_wsf2015.py)              | 
| World Settlement Footprint (WSF) 2019         | [EOC Geoservice](https://geoservice.dlr.de/web/maps/eoc:wsf2019)                       | [download_wsf2019.py](scripts/download_wsf2019.py)              | 
| WSF Evolution (1985-2015)                     | [EOC Geoservice](https://geoservice.dlr.de/web/maps/eoc:wsf_evolution)                 | [download_wsf_evolution.py](scripts/download_wsf_evolution.py)  | 
| WSF 3D (Building Volume/Height)               | [EOC Geoservice](https://geoservice.dlr.de/web/maps/eoc:wsf3d)                         | [download_wsf3d.py](scripts/download_wsf3d.py)                  | 
| Global Human Settlement Layer (GHSL) Built-up | [JRC GHSL](https://ghsl.jrc.ec.europa.eu/ghs_bu.php)                                   | [download_ghs_built.sh](scripts/download_ghs_built.sh)          | 
| GHS-SMOD (Settlement Model)                   | [JRC GHSL](https://ghsl.jrc.ec.europa.eu/ghs_smod.php)                                 | [download_ghs_smod.sh](scripts/download_ghs_smod.sh)            | 
|                                               |                                                                                        |                                                                 |
|                                               |                                                                                        |                                                                 |
| **EMBEDDING SPACES & FOUNDATION MODELS**      |                                                                                        |                                                                 | 
| AlphaEarth Embeddings                         | *Internal/Requires Access*                                                             | [fetch_alphaearth_embeds.py](scripts/fetch_alphaearth_embeds.py) | 
| Tessera Embeddings                            | *Internal/Requires Access*                                                             | [fetch_tessera_embeds.py](scripts/fetch_tessera_embeds.py)      | 
| Satlas (Super-Resolution/Embeddings)          | [Satlas AllenAI](https://satlas.allenai.org/)                                          | [download_satlas.py](scripts/download_satlas.py)                | 
| Prithvi (NASA/IBM Geospatial FM)              | [Hugging Face](https://huggingface.co/ibm-nasa-geospatial)                             | [download_prithvi.py](scripts/download_prithvi.py)              | 
|                                               |                                                                                        |                                                                 |
|                                               |                                                                                        |                                                                 |
| **LAND COVER CLASSIFICATIONS**                |                                                                                        |                                                                 | 
| ESA WorldCover 10m                            | [ESA WorldCover](https://esa-worldcover.org/en)                                        | [download_worldcover.py](scripts/download_worldcover.py)        | 
| Google Dynamic World                          | [Dynamic World](https://dynamicworld.app/)                                             | [download_dynamic_world.py](scripts/download_dynamic_world.py)  | 
|                                               |                                                                                        |                                                                 |
|                                               |                                                                                        |                                                                 |
| **BUILDINGS & INFRASTRUCTURE**                |                                                                                        |                                                                 | 
| Google Open Buildings (Africa/Asia/LatAm)     | [Google Research](https://sites.research.google/open-buildings/)                       | [download_open_buildings.py](scripts/download_open_buildings.py) | 
| Microsoft Global Building Footprints          | [GitHub / Planetary Computer](https://github.com/microsoft/GlobalMLBuildingFootprints) | [download_ms_buildings.py](scripts/download_ms_buildings.py)    | 
| GRID3 (Geo-Referenced Infrastructure)         | [GRID3 Data Hub](https://grid3.org/data)                                               | [download_grid3_pois.py](scripts/download_grid3_pois.py)        | 
|                                               |                                                                                        |                                                                 |
|                                               |                                                                                        |                                                                 |
| **POPULATION & DEMOGRAPHICS**                 |                                                                                        |                                                                 | 
| WorldPop (Unconstrained & Constrained)        | [WorldPop Data](https://www.worldpop.org/)                                             | [download_worldpop.py](scripts/download_worldpop.py)            | 
| GHS-POP (Population Grid)                     | [JRC GHSL](https://ghsl.jrc.ec.europa.eu/ghs_pop.php)                                  | [download_ghs_pop.sh](scripts/download_ghs_pop.sh)              | 
| Meta HRSL (High-Resolution Settlement)        | [CIESIN / Meta](https://ciesin.columbia.edu/data/hrsl/)                                | [download_meta_hrsl.py](scripts/download_meta_hrsl.py)          | 
|                                               |                                                                                        |                                                                 |
|                                               |                                                                                        |                                                                 |
| **NIGHTTIME LIGHTS & SOCIO-ECONOMIC**         |                                                                                        |                                                                 | 
| VIIRS Nighttime Lights (VNP46A1/A2)           | [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/)                             | [download_viirs_ntl.py](scripts/download_viirs_ntl.py)          | 