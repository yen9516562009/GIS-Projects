# 2015 US Airline Origin-Destination (OD) Visualization - San Diego
This project explores the utility of [kepler.gl](https://kepler.gl/demo), a powerful open-source geospatial analysis tool for large-scale data sets.
An interactive Arc layer visuzlizes the US OD pairs with passenger miles in San Diego, acquired from [US Airline Route Segments 2015](https://data.world/garyhoov/us-airline-route-segments-2015).
[Arc layers](https://docs.kepler.gl/docs/user-guides/c-types-of-layers/b-arc) draw an arc between two points. The tallest arc represents the greatest distance. The thicker arc stands for higher passenger miles.

![alt text](https://github.com/yen9516562009/GIS-Projects/US-Airline-OD-Visualization-San-Diego-CA/san_diego_viz_screenshot.png?raw=true)

## Description of Contents
* `data`: US Airline Route Segments 2015 dataset
* `src`: a script to create San Diego subset with geocoded OD lat\lon.
* `output`: an output csv that is ready for kepler.gl visualization.
* `viz`: contains the resulting arc layer visualization (.html)
