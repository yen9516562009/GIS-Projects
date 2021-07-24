# -*- coding: utf-8 -*-
"""
US COVID-19 Analysis
- As of 07/22/2021

@author: Jeff Yen
"""


import os
import requests
import datetime as dt
import pandas as pd
import geopandas as gpd

# Set workspace to current script directory
os.chdir(os.path.dirname(os.path.abspath('__file__')))

# Load COVID-19 Case data
county = pd.read_csv(r"..\data\us-counties.csv")
ca = county.query("state == 'California'")


# Use GOOGLE Geocoding API
API_KEY = 'AIzaSyCavG762JLQ41LEUJVlFllC--sxmeprlCk'
base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

def get_lat_lng(address):
    endpoint = f"{base_url}?address={address}&key={API_KEY}"
    resultDF = requests.get(endpoint).json()['results'][0]
    lat = resultDF['geometry']['location']['lat']
    lng = resultDF['geometry']['location']['lng']
    centroid = [address, lat, lng]
    
    return centroid

# # Get all US counties centroid
# county['address'] = county.county + ', ' + county.state
# us_county = county.groupby('address').size().reset_index()
# cty_centroids = []
# for county in us_county['address']:
#     cty_centroids.append(get_lat_lng(county))

# # Convert result list to pandas DataFrame
# cty_centroidsDF = pd.DataFrame(cty_centroids, columns=['address', 'lat', 'lng'])
# resultDF = us_county.merge(cty_centroidsDF, on='address')
# resultDF.to_csv(r"..\output\COVID-19_US_County_2020-2021.csv", index=False)


# Get all CA counties centroid
ca['address'] = ca.county + ', ' + ca.state
ca_county = ca.groupby('address').size().reset_index()
cty_centroids = []
for county in ca_county['address']:
    cty_centroids.append(get_lat_lng(county))

# Convert result list to pandas DataFrame
cty_centroidsDF = pd.DataFrame(cty_centroids, columns=['address', 'lat', 'lng'])
resultDF = ca.merge(cty_centroidsDF, on='address')
# resultDF['date'] = resultDF['date'].str.replace('-', '/')
resultDF['date'] = pd.to_datetime(resultDF['date']).dt.strftime('%Y/%m/%d %H:%M')
# resultDF = gpd.GeoDataFrame(resultDF, geometry=gpd.points_from_xy(resultDF.lng, resultDF.lat))
resultDF.to_csv(r"..\output\COVID-19 CA_County_2020-2021.csv", index=False)