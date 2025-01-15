# Citi Bike Data Analysis and Dashboard

## Project Overview  
This project analyzes Citi Bike's bike-sharing data from 2022 in New York City to uncover key insights into user behavior, seasonal patterns, and station distribution challenges. The analysis integrates weather data from NOAA to study the influence of weather conditions on bike usage. The project aims to assist in optimizing bike availability and distribution, ensuring better service for users.

## Objective  
The primary objective is to conduct a descriptive analysis of Citi Bike trips across NYC and create an interactive dashboard that presents the findings to help business strategists make informed decisions.

## Key Insights  
- Identified high-demand bike stations and popular routes.  
- Analyzed seasonal patterns in bike usage and their correlation with weather conditions.  
- Uncovered distribution challenges, such as over-utilized or under-utilized stations.  
- Provided actionable insights for improving bike availability and distribution strategies.

## Tools and Technologies  
- **Data Analysis:** Python, Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn, Plotly, Kepler.gl  
- **Geospatial Analysis:** Geopandas, Kepler.gl  
- **Data Sourcing:** Citi Bike open data, NOAA API for weather data  
- **Environment:** Jupyter Notebook  

## Data  
The analysis uses open-source data provided by Citi Bike for the year 2022. Additional weather data was sourced via the NOAA API to enrich the dataset.

## Features  
1. **Descriptive Analysis:**  
   Aggregated and summarized bike trip data to identify key trends and patterns.  
2. **Geospatial Visualization:**  
   Created geographic plots to highlight problem areas in station distribution and popular routes using Kepler.gl.  
3. **Interactive Dashboard:**  
   Developed an interactive dashboard with clear sections for each analysis category, designed for business strategists.

## How I created this Repository 
1. Clone the repository.  
2. Ensure you have Python installed along with the required libraries listed in `requirements.txt`.  
3. Download Citi Bike data from [Citi Bike Data](https://s3.amazonaws.com/tripdata/index.html) and gather weather data using the NOAA API.  
4. Run the Jupyter Notebook to execute the analysis and generate the visualizations.

## Deliverables  
- **Interactive Dashboard:** Displays bike usage trends, weather patterns, and key metrics.  
- **Recommendations Report:** Provides actionable steps to improve Citi Bike’s distribution strategy.

## Limitations  
- The analysis covers data from 2022, so recent trends may not be reflected.  
- Weather data was sourced from NOAA, but microclimate effects may not be fully captured.

## Future Enhancements  
- Incorporate real-time data for live dashboard updates.  
- Explore predictive analytics to forecast demand based on weather and time of day.
