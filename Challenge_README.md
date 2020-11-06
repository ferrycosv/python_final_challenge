# 3D House Project

- Repository: `Data tools`
- Type of Challenge: `Learning & Consolidation`
- Duration: `2 weeks`
- Deadline: `20/11/20 9:00 AM`
- Deployment strategy :
	 Github page
	| Powerpoint
	| Jupyter Notebook
	| Webpage
	| App
- Team challenge : `solo`

## Mission objectives 
Consolidate the knowledge in Python, specifically in :
- NumPy
- Pandas 
- Matplotlib

## Learning Objectives 

- to be able to search and implement new libraries
- to be able to read and use shapefiles
- to be able to read and use geoTIFFs 
- to be able to render a 3D plot
- to be able to present a final product


## The Mission

<img src="assets/business.jpg" align="right" width="200" />

> "Hey you, you look like you know what you're doing. I've got the perfect business opportunity for you!"
> "I sto- uh 'got' this perfectly usable dataset of **geospatial** data from the last company I worked at."
> "I've got the best idea for it: you make a little program that accepts a **coordinate** and shows a nice **3D plot** of the **house** at the location."
> "What do you mean google already does this? That's not the point, our company is going to do it way better!"
> "C'mon, I believe in you, we can do this. And by we I mean you, obviously."


### Must-have features

- 3D lookup of houses.

### Nice-to-have features

- Optimize your solution to have the result as fast as possible.
- Features like the living area of the house in m², how many estimated floors, if there is a pool, the vegetation in the neighborhood, etc... 
- Better visualization.

### Miscellaneous information

#### What is LIDAR ?

LIDAR is a method to measure distance using light. The device will illuminate a target with a laser light and a sensor will measure the reflection. Differences in wavelength and return times will be used to get 3D representations of an area.

Here is a LIDAR segmentation :

![Lidar Segmentation](./assets/DSM.jpg)

With those points clouds we can easily identify houses, vegetation, roads, etc...

The results we're interested in are DSM (Digital Surface Map) and DTM (Digital Terrain Map).

Which are already computed and available here :

- [DSM](http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dsm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DSM,%20raster,%201m)
- [DTM](http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dtm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DTM,%20raster,%201m)

What's the difference? well, there are some [slight differences](https://gisgeography.com/dem-dsm-dtm-differences/)

## Deliverables

1. Publish your source code on the GitHub repository.
2. Pimp up the readme file:
	- What, Why, When, How, Who.
	- Pending things to do
3. Show us your results in a nice presentation.
4. Show us a live demo

### Steps
1. Create the repository
2. Study the request (What & Why ?)
3. Download the maps
4. Identify technical challenges (How ?)

## Evaluation criterias
1. It works (no bugs in the console, no error)
2. You use Git from the start and during the entire process of the development (at least one push per day)
3. You convince us during the final presentation

## A final note of encouragement

![You've got this!](https://media.giphy.com/media/yoJC2K6rCzwNY2EngA/giphy.gif)
