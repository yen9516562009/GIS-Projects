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
county_case['year-month'] = pd.to_datetime(county_case['date']).dt.strftime('%Y/%m') # by month
county_case = county_case.groupby(['year-month', 'state', 'county'])['cases', 'deaths'].sum().reset_index()
# county_case = county_case.loc[pd.DatetimeIndex(county_case['year-month']).year == 2020] # use 2020 only

# cases and deaths monthly difference calculation
county_case = county_case.sort_values(['state','county','year-month'], ascending = (True, True, True))
county_case['case_delta'] = county_case.cases.diff(periods = 1)
county_case['death_delta'] = county_case.deaths.diff(periods = 1)
county_case['death_rate'] = county_case.deaths / county_case.cases * 100

# Load US county and state geography
county = gpd.read_file(r"..\data\cb_2018_us_county_500k.shp")
state = gpd.read_file(r"..\data\cb_2018_us_state_500k.shp")
geo = county.merge(state[['STATEFP', 'NAME']], on='STATEFP')
geo = geo.rename(columns={'NAME_x':'COUNTY', 'NAME_y':'STATE'})

# Get lat/lng
geo['lat'] = geo.geometry.centroid.y
geo['lng'] = geo.geometry.centroid.x

# merge county case with geo
resultDF = county_case.merge(geo[['COUNTY', 'lat', 'lng']], left_on='county', right_on='COUNTY')
colOfInterest = list(county_case.columns) + ['lat', 'lng']
resultDF = resultDF[colOfInterest]

# Export
resultDF['year-month'] = pd.to_datetime(resultDF['year-month']).dt.strftime('%Y/%m/%d %H:%M')
resultDF.to_csv(r"..\output\COVID-19 US_County_monthly.csv", index=False)

