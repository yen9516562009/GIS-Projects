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
county_case = county_case.query("county != 'Unknown'") # exclude 'Unknown county'

# Aggregate cases and deaths by year-month, state and county
county_case['year-month'] = pd.to_datetime(county_case['date']).dt.strftime('%Y/%m')
county_case = county_case.groupby(['state', 'county', 'year-month'])['cases', 'deaths'].sum().reset_index()

# Calculate monthly cases and deaths difference by state and county
county_case['case_delta'] = county_case.cases.diff(periods = 1)
county_case['death_delta'] = county_case.deaths.diff(periods = 1)

# Calculate monthly death_rate by state and county
county_case['death_rate'] = (county_case.deaths / county_case.cases * 100).round(1)

# Load US county and state geography
county = gpd.read_file(r"..\data\cb_2018_us_county_500k.shp")
state = gpd.read_file(r"..\data\cb_2018_us_state_500k.shp")
geo = county.merge(state[['STATEFP', 'NAME']], on='STATEFP') # remain county geometry
geo = geo.rename(columns={'NAME_x':'COUNTY', 'NAME_y':'STATE'})

# Extract lat/lng
geo['lat'] = geo.geometry.centroid.y
geo['lng'] = geo.geometry.centroid.x

# Merge county case with geography attributes
resultDF = county_case.merge(geo[['COUNTY', 'STATE', 'lat', 'lng', 'geometry']],
                             left_on=['county', 'state'],
                             right_on=['COUNTY', 'STATE'],
                             how = 'left')
colOfInterest = list(county_case.columns) + ['lat', 'lng'] # include 'geometry' if want to map this dataset by county boundary
resultDF = resultDF[colOfInterest]

# Convert string date to datetime (required by kepler.gl Time Playback feature)
resultDF['year-month'] = pd.to_datetime(resultDF['year-month']).dt.strftime('%Y/%m/%d %H:%M')

# Export result to csv
resultDF.to_csv(r"..\output\COVID-19 US_County_monthly.csv", index=False)
