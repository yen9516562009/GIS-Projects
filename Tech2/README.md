# 2015 US Airline Origin-Destination (OD) Visualization - San Diego

This project explores the utility of [kepler.gl](https://kepler.gl/demo), a powerful open-source geospatial analysis tool for large-scale data sets.
An interactive [Arc layer](https://docs.kepler.gl/docs/user-guides/c-types-of-layers/b-arc) visuzlizes the US OD pairs with passenger miles in San Diego, acquired from [US Airline Route Segments 2015](https://data.world/garyhoov/us-airline-route-segments-2015). Arc layers draw an arc between two points. The thicker arc stands for higher passenger miles. The tallest arc represents the greatest distance.

## Description of Contents

* `data`:
  * **City Pairs all airlines ranked by volume.xlsx**: US Airline Route Segments 2015 dataset
* `src`:
  * **data_processing.py**: a script to create San Diego subset with geocoded OD lat\lon.
  * `utilities`:
    * **geocoding.py**: a script to geocode address using GOOGLE API
* `output`:
  * **2015 San Diego Flight OD.csv**: an output csv that is ready for kepler.gl visualization.
* `viz`:
  * **2015 San Diego Flight OD Visualization.html**: an Arc layer visualization in html format.
  * **san_diego_viz_screenshot.png**: a project sreenshot.

## Project Questions
1.
how source products used?
what are properties of the final product?
devise an output file name for the aggregated output product.

2.
write README file
## SDG
SDG stands for Sustainable Development Goal
Access:
[SDG6.6.1]https://www.sdg661.app/downloads
SHP & GeoTIFF available
The following provides global scale tabular comma separated value data for each aggregation type.
            National boundaries (GAUL 0). 1984 - 2019
            Administrative level 1 (GAUL 1). 1984 - 2019
            Administrative level 2 (GAUL 2). 1984 - 2019
            HydroBASIN, Level 6. 1984 - 2019

Geotiffs are available for each country based on GAUL 0 boundaries. Each country is a collection of 4 different types of GeoTiffs with data from 2000-2018. Larger countries are split into a series of tiles. 


[Global SDG database](https://www.google.com/url?q=https%3A%2F%2Funstats.un.org%2Fsdgs%2Findicators%2Fdatabase%2F&sa=D&sntz=1&usg=AFQjCNE40ig-41zdKtXeezTQnnq81iQa2A)

## MOD11A1


## Data Processing
"""
These steps were used to generate temperature over water extent:
"""
1. Open SDG and MODIS data via rasterio
2. 
3. resolution of SDG data?

3.
Make a list of notes and questions to be given to the data analyst to improve product


## Workflow
study SDG (Surface Water Extent) and MOD11A1 (Land Surface Temperature)
