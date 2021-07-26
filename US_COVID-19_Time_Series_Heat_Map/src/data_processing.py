# -*- coding: utf-8 -*-
"""
US Airline OD Visualization - San Diego, CA

@author: Jeff Yen
"""


import os
import pandas as pd
from utilities.geocoding import geocoding

# Set workspace to current script directory
os.chdir(os.path.dirname(os.path.abspath('__file__')))

# Load COVID-19 Case data
odData = pd.read_excel(r"..\data\City Pairs all airlines ranked by volume.xlsx")
sd = odData.query("ORIGIN_CITY_NAME == 'San Diego, CA'")

# Extraxt unique OD pairs
odPair = sd.groupby(['ORIGIN_CITY_NAME', 'DEST_CITY_NAME']).size().reset_index(name = 'Frequency')

# Geocode OD city XY location
origin = geocoding(list(odPair.ORIGIN_CITY_NAME.unique())[0])
sd['ori_lat'] = origin[1]
sd['ori_lng'] = origin[2]


destination = []
for dest in odPair['DEST_CITY_NAME']:
    destination.append(geocoding(dest))

# Convert destination list to pd.df
destDF = pd.DataFrame(destination, columns=['DEST_CITY_NAME', 'dest_lat', 'dest_lng'])
resultDF = sd.merge(destDF, on='DEST_CITY_NAME')

# Export result
resultDF.to_csv(r"..\output\2015 San Diego Flight OD.csv", index=False)