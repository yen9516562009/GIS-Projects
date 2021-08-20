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

3.
Make a list of notes and questions to be given to the data analyst to improve product


## Workflow
study SDG and MOD11A1 datasets
