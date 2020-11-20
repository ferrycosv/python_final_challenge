import getopt
import sys

import georasters as gr
import numpy as np
import plotly.graph_objects as go
import pyproj
from dms2dec.dms_convert import dms2dec


def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print('challenge.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('challenge.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg

    if inputfile == '':
        print('challenge.py -i <inputfile>')
        sys.exit(2)
    print('Welcome to my python challenge CLI program to plot a DSM given a set of coordinates in DMS')

    # Read the GeoTiff file and extract properties
    # raster = os.path.join(os.path.dirname(os.path.abspath(__file__)), inputfile)
    # raster = os.path.join(DATA, inputfile)
    info = gr.get_geo_info(inputfile)
    crs = info[4]
    crs_name = crs.GetAttrValue('projcs')
    units = crs.GetAttrValue("PROJCS|UNIT", 0)
    crs_authority = [crs.GetAttrValue("PROJCS|AUTHORITY", 0), crs.GetAttrValue("PROJCS|AUTHORITY", 1)]
    complete_file = gr.from_file(inputfile)

    # Ask user to input latitude value in DMS and calculate decimal value
    print('Please input the coordinates')
    print('We will start by the latitude...')
    degrees = input('Please input the degrees value (number ex. 51)\n')
    minutes = input('Please input the minutes value (number ex. 12)\n')
    seconds = input('Please input the minutes value (number ex. 31.8)\n')
    heading = input('Please input the heading (options N, S)\n')

    # degrees = 51
    # minutes = 12
    # seconds = 34.1
    # heading = 'N'
    latitude_str = f'''{degrees}°{minutes}'{seconds}"{heading}'''
    latitude = dms2dec(latitude_str)

    # Ask user to input longitude value in DMS and calculate decimal value
    print('Now please input the longitude coordinates...')
    degrees = input('Please input the degrees value (number ex. 3)\n')
    minutes = input('Please input the minutes value (number ex. 13)\n')
    seconds = input('Please input the minutes value (number ex. 27.4)\n')
    heading = input('Please input the heading (options W, E)\n')

    # degrees = 3
    # minutes = 13
    # seconds = 22.5
    # heading = 'E'
    longitude_str = f'''{degrees}°{minutes}'{seconds}"{heading}'''
    longitude = dms2dec(longitude_str)

    # Transform the decimal coordinates to the projection extracted from the file properties
    transformer = pyproj.Transformer.from_crs('epsg:4326', f'{crs_authority[0]}:{crs_authority[1]}')
    lambert_x, lambert_y = transformer.transform(latitude, longitude)
    print(f'The transformed values to {crs_authority[0]}:{crs_authority[1]} are [X:{lambert_x}, Y:{lambert_y}]')

    # Ask user to provide a radius to filter raster file
    radius = int(input(f'Please input the radius to filter in {units}s (integer ex. 100)\n'))
    # radius = 50

    # Extract the area of interest from the raster file
    trimmed_file = complete_file.extract(lambert_x, lambert_y, radius=radius)
    # trimmed_file.plot()

    # Show to user the trimmed raster file
    # plt.show()

    # Convert raster file to pandas dataframe
    df = trimmed_file.to_pandas()

    # Process the data frame to create the inputs for the surface plot
    z = []
    x = df['col'].unique()
    y = df['row'].unique()
    for i in x:
        row = df.query(f'col == {i}')['value'].to_list()
        z.append(row)
    z = np.array(z)

    # Plot the meshgrid from the 3D data points
    layout = go.Layout(scene=dict(aspectmode='data'),
                       title=f'Center coordinates: [{latitude_str}, {longitude_str}] Radius = {radius} {units}s',
                       autosize=True)
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='dense', showlegend=False)], layout=layout)
    fig.show()

    print('Thank you for using my program, I hope it was useful to you!')
    print('Created by: Francisco Fernandez')
    print('Copyright 2020')


if __name__ == "__main__":
    main(sys.argv[1:])
