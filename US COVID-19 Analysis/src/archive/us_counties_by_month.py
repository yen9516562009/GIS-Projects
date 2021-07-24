# -*- coding: utf-8 -*-
"""
US COVID-19 Analysis
- As of 07/22/2021

@author: Jeff Yen
"""


import os
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

# by month
resultDF['year-month'] = pd.to_datetime(resultDF['date']).dt.strftime('%Y/%m')
resultDF = resultDF.groupby(['year-month', 'state', 'county'])['cases', 'deaths'].sum().reset_index()

#
resultDF = resultDF.sort_values(['year-month','state','county'], ascending = (True, True, True))
resultDF['case_delta'] = resultDF.cases.diff(periods=-1)
resultDF['death_delta'] = resultDF.deaths.diff(periods=-1)

# Convert result list to pandas DataFrame
resultDF = resultDF.merge(geo[['COUNTY', 'lat', 'lng', 'geometry']], left_on='county', right_on='COUNTY')

# Export
resultDF['year-month'] = pd.to_datetime(resultDF['year-month']).dt.strftime('%Y/%m/%d %H:%M')
resultDF.to_csv(r"..\output\COVID-19 US_County_monthly.csv", index=False)

