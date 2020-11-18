import georasters as gr
import os
import matplotlib.pyplot as plt
from dms2dec.dms_convert import dms2dec
import pyproj


print('Welcome to my python challenge CLI program to plot a DSM given a set of coordinates in DMS')
# Read the GeoTiff file and extract properties
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
raster = os.path.join(DATA, 'DHMVIIDSMRAS1m_k13.tif')
info = gr.get_geo_info(raster)
crs = info[4]
crs_name = crs.GetAttrValue('projcs')
units = crs.GetAttrValue("PROJCS|UNIT", 0)
crs_authority = [crs.GetAttrValue("PROJCS|AUTHORITY", 0), crs.GetAttrValue("PROJCS|AUTHORITY", 1)]
complete_file = gr.from_file(raster)

# Ask user to input latitude value in DMS and calculate decimal value
print('Please input the coordinates')
print('We will start by the latitude...')
degrees = input('Please input the degrees value (number ex. 51)\n')
minutes = input('Please input the minutes value (number ex. 12)\n')
seconds = input('Please input the minutes value (number ex. 31.8)\n')
heading = input('Please input the heading (options N, S)\n')
latitude = dms2dec(f'''{degrees}°{minutes}'{seconds}"{heading}''')

# Ask user to input longitude value in DMS and calculate decimal value
print('Now please input the longitude coordinates...')
degrees = input('Please input the degrees value (number ex. 3)\n')
minutes = input('Please input the minutes value (number ex. 13)\n')
seconds = input('Please input the minutes value (number ex. 27.4)\n')
heading = input('Please input the heading (options W, E)\n')

longitude = dms2dec(f'''{degrees}°{minutes}'{seconds}"{heading}''')

# Transform the decimal coordinates to the projection extracted from the file properties
transformer = pyproj.Transformer.from_crs('epsg:4326', f'{crs_authority[0]}:{crs_authority[1]}')
lambert_x, lambert_y = transformer.transform(latitude, longitude)
print(f'The transformed values to {crs_authority[0]}:{crs_authority[1]} are [X:{lambert_x}, Y:{lambert_y}]')

# Ask user to provide a radius to filter raster file
radius = int(input(f'Please input the radius to filter in {units}s (integer ex. 100)\n'))

# Extract the area of interest from the raster file
trimmed_file = complete_file.extract(lambert_x, lambert_y, radius=radius)
trimmed_file.plot()

# Show to user the trimmed raster file
plt.show()

# Convert raster file to pandas dataframe
df = trimmed_file.to_pandas()
print(df.head())
print('Thank you for using my program, I hope it was useful to you!')
print('Created by: Francisco Fernandez')
print('Copyright 2020')
