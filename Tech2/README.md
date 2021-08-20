# Generate a Surface Water Temperature Product with a Monthly Temporal Resolution
This is the project for the Element 84 Tech Screen.

## Project Questions
1.
how source products used?
what are properties of the final product?
devise an output file name for the aggregated output product.

## Data Acquisition
### SDG
SDG stands for Sustainable Development Goal.

* Access: [SDG6.6.1 - Downloads](https://www.sdg661.app/downloads)

* Format: Shapefiles & GeoTiff available

### MOD11A1
The MOD11A1 Version 6 product provides daily per-pixel Land Surface Temperature and Emissivity (LST&E) with 1 kilometer (km) spatial resolution in a 1,200 by 1,200 km grid.

* Access: [MOD11A1v006 Version 6 product](https://lpdaac.usgs.gov/products/mod11a1v006/)

* Format: hdf


## Data Processing
These steps were used to generate temperature over water extent:
1. Open SDG data via rasterio.
2. Downsample and re-project SDG data to WGS84 (EPSG 4326).
3. Open MODIS data via rasterio.
4. Re-project the MODIS data to match the projection and resolution of the downsampled
SDG product.
5. Crop the temperature data to the water extent.
6. Repeat steps 3-5 for files for Julian days 121 to 151, then results averaged and written
as one file.

**Julian Days
[Julian Day Calendar] (https://ltdr.modaps.eosdis.nasa.gov/browse/calendar.html)

3.

The following lists of notes and questions are given to the data analyst to improve product
## Questions
* `How to determine the downsample spatial resolution for SDG product?`

## Notes
* `Julian days 121 - 151 in leap years covers the end of April and most of May. However in regular years, it ocvers the entire May.`
* `In Python sample code, analysts may initialize a result list and use a loop function to iterate the following procedures:`
   * Reproject and downsample the MODIS product.
   * Crop the resulting MODIS data to water extent (i.e., SDG extent).
   * Save the cropped MODIS data to the result list.
* `Finally, do simple average by each cropped MODIS data in the result list and export to GeoTIFF`


## Workflow
study SDG (Surface Water Extent) and MOD11A1 (Land Surface Temperature)
understand Python sample code (any improvement?)


