# -*- coding: utf-8 -*-
"""
US COVID-19 Analysis
- As of 07/22/2021

@author: Jeff Yen
"""


import os
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

# Set workspace to current script directory
os.chdir(os.path.dirname(os.path.abspath('__file__')))

# Load COVID-19 Case data
county_case = pd.read_csv(r"..\data\us-counties.csv")
county_case['date'] = pd.to_datetime(county_case['date']).dt.strftime('%Y/%m/%d %H:%M')

# Load US county and state geography
county = gpd.read_file(r"..\data\cb_2018_us_county_500k.shp")
state = gpd.read_file(r"..\data\cb_2018_us_state_500k.shp")
geo = county.merge(state[['STATEFP', 'NAME']], on='STATEFP')
geo = geo.rename(columns={'NAME_x':'COUNTY', 'NAME_y':'STATE'})

# Get lat/lng
geo['lat'] = geo.geometry.centroid.y
geo['lng'] = geo.geometry.centroid.x
geo['geometry'] = geo.geometry.centroid

# Convert result list to pandas DataFrame
resultDF = geo[['COUNTY', 'lat', 'lng', 'geometry']].merge(county_case, left_on='COUNTY', right_on='county')
colOfInterest = list(county_case.columns) + ['lat', 'lng', 'geometry']
resultDF = resultDF[colOfInterest]

#
resultDF = resultDF.sort_values(['date','state','county'], ascending = (True, True, True))
resultDF['case_delta'] = resultDF.cases.diff(periods=-1)
resultDF['death_delta'] = resultDF.deaths.diff(periods=-1)


# 
# result20 = resultDF.loc[pd.DatetimeIndex(resultDF['date']).year == 2020]
# result21 = resultDF.loc[pd.DatetimeIndex(resultDF['date']).year == 2021]
test = resultDF.loc[(pd.DatetimeIndex(resultDF['date']).year == 2020)&
                    (pd.DatetimeIndex(resultDF['date']).month >= 10)]

# # Export
# result20.to_csv(r"..\output\COVID-19 US_County_2020.csv", index=False)
# result21.to_csv(r"..\output\COVID-19 US_County_2021.csv", index=False)
# test.to_csv(r"..\output\COVID-19 US_County_01-062020.csv", index=False)


df = test.query("date == '2020/12/01 00:00'")
df.to_csv("df.csv")
import folium
from folium.plugins import HeatMap

basemap = folium.Map(location=[48, -102], zoom_start=3)

heatmap_data = list(map(list, zip(df['lat'], df['lng'])))

HeatMap(heatmap_data, radius=15, gradient={'0':'Navy', '0.25':'Blue','0.5':'Green', '0.75':'Yellow','1': 'Red'}).add_to(basemap)

basemap.save("mymap.html")

