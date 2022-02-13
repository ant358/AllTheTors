import pandas as pd
import numpy as np
from OSGridConverter import grid2latlong

df = pd.read_csv('AllTheTors_grid_ref.csv')
print(df.head())

# convert the grid references to latitude and longitude
def get_lat(row):
    l= grid2latlong(row['Grid'])
    return l.latitude

def get_long(row):
    l= grid2latlong(row['Grid'])
    return l.longitude

df['latitude'] = df.apply(lambda row: get_lat(row), axis=1)
df['longitude'] = df.apply(lambda row: get_long(row), axis=1)
print(df.head())

df['Completed'] = 0

df.to_csv('AllTheTors_lat_long.csv', index=False)