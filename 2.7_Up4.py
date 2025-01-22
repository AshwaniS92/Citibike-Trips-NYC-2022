#!/usr/bin/env python
# coding: utf-8

# ## Imoprting Libraries

# In[10]:

import os
import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from datetime import datetime as dt
from numerize.numerize import numerize
from PIL import Image


# In[11]:


########################## Import data ###########################################################################################

# Path to the exported CSV file
file_path = '/Users/ashwanisherawat/citibike_env/bin/top20.csv'


# In[12]:


# Path to the exported CSV file
path = '/Users/ashwanisherawat/citibike_env/bin/debug_combined_df.csv'
#import os module
path = f"{os.getcwd()}/debug_combined_df.csv"
file_path = f"{os.getcwd()}/top20.csv"

bikes = f"{os.getcwd()}/istockphoto-2181208335-612x612.jpg"
myImage = f"{os.getcwd()}/Citi bike images/istockphoto-2190292731-612x612.jpg"


# Resolve the image paths (relative to the current working directory)
bikes = "istockphoto-2181208335-612x612.jpg"
myImage = "istockphoto-2190292731-612x612.jpg"

# Check if the images exist in the current directory
if os.path.exists(bikes_path) and os.path.exists(myImage):
    # Load and display the images
    bikes = Image.open(bikes)
    myImage = Image.open(myImage)
    
    st.image(bikes, caption="Bikes Image")
    st.image(myImage, caption="My Image")
else:
    # Show error messages if the files are missing
    if not os.path.exists(bikes):
        st.error(f"Image not found: {bikes}")
    if not os.path.exists(myImage):
        st.error(f"Image not found: {myImage}")

# In[13]:




# Read the Pickle file into a DataFrame
top20 = pd.read_csv(file_path)


# In[14]:


# Read the Pickle file into a DataFrame
df = pd.read_csv(path)


# In[15]:


# Generate all column names
column_names = df.columns

# Display the column names
print("Column names:")
for col in column_names:
    print(col)


# In[16]:


########################### Initial settings for the dashboard ####################################################


st.set_page_config(page_title = 'Citi Bikes Strategy Dashboard', layout='wide')
st.title("Citi Bikes Strategy Dashboard")

# Define side bar
st.sidebar.title("Aspect Selector")
page = st.sidebar.selectbox('Select an aspect of the analysis',
  ["Intro page","Weather component and bike usage",
   "Most popular stations",
    "Interactive map with aggregated bike trips", "Recommendations"])


# In[17]:


# Define the pages

# Intro page
if page == "Intro page":
    st.markdown("#### This dashboard aims at providing helpful insights on the expansion problems Citi Bikes currently faces.")
    st.markdown("Right now, Citi bikes runs into a situation where customers complain about bikes not being available at certain times. This analysis will look at the potential reasons behind this. The dashboard is separated into 4 sections:")
    st.markdown("- Most popular stations")
    st.markdown("- Weather component and bike usage")
    st.markdown("- Interactive map with aggregated bike trips")
    st.markdown("- Recommendations")
    st.markdown("The dropdown menu on the left 'Aspect Selector' will take you to the different aspects of the analysis our team looked at.")

    myImage = Image.open("/Users/ashwanisherawat/citibike_env/bin/Citi bike images/istockphoto-2190292731-612x612.jpg") 
    st.image(myImage)

# Weather component and bike usage
elif page == "Weather component and bike usage":
    fig_2 = make_subplots(specs=[[{"secondary_y": True}]])

    fig_2.add_trace(
        go.Scatter(x=df['date'], y=df['trip_count'], name='Daily bike rides', marker={'color': 'blue'}),
        secondary_y=False
    )

    fig_2.add_trace(
        go.Scatter(x=df['date'], y=df['Avg Temperature'], name='Daily temperature', marker={'color': 'red'}),
        secondary_y=True
    )

    fig_2.update_layout(
        title='Daily bike trips and temperatures in 2022',
        height=400
    )

    st.plotly_chart(fig_2, use_container_width=True)
    st.markdown("There is an obvious correlation between the rise and drop of temperatures and their relationship with the frequency of bike trips taken daily. As temperatures plunge, so does bike usage. This insight indicates that the shortage problem may be prevalent merely in the warmer months, approximately from May to October.")

# Most popular stations page
elif page == "Most popular stations":
    # Define the total rides
    total_rides = float(top20['value'].sum())
    st.metric(label='Total Bike Rides', value=numerize(total_rides))

    # Bar chart
    top20 = top20.nlargest(20, 'value')  # Ensure top 20 stations are selected
    fig = go.Figure(
        go.Bar(
            x=top20['value'],
            y=top20['start_station_name'],
            orientation='h',  # Horizontal orientation
            marker={'color': top20['value'], 'colorscale': 'Blues'}
        )
    )
    fig.update_layout(
        title='Top 20 most popular bike stations',
        xaxis_title='Sum of trips',
        yaxis_title='Start stations',
        width=900,
        height=600
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("From the bar chart it is clear that there are some start stations that are more popular than others. In the top 3, we can see W 21 St & 6 Ave, West St & Chambers St, and Broadway & W 58 St. There is a significant jump between the highest and lowest bars of the plot, indicating clear preferences for the leading stations. This is a finding that we could cross-reference with the interactive map that you can access through the sidebar select box.")

# Interactive map with aggregated bike trips
elif page == "Interactive map with aggregated bike trips":
    st.write("Interactive map showing aggregated bike trips over New York")

    path_to_html = "/Users/ashwanisherawat/citibike_env/bin/Citi Bike Trips Aggregated_50000.html"

    # Read file and keep in variable
    with open(path_to_html, 'r') as f:
        html_data = f.read()

    # Show in webpage
    st.header("Aggregated Bike Trips in New York")
    st.components.v1.html(html_data, height=1000)
    st.markdown("#### Using the filter on the left-hand side of the map we can check whether the most popular start stations also appear in the most popular trips.")
    st.markdown("The most popular start stations are:")
    st.markdown("Streeter Drive/Grand Avenue, Canal Street/Adams Street as well as Clinton Street/Madison Street.")
 
    st.markdown("### Key Observations:")
    st.markdown("""
    1. **High Activity in Manhattan**: Central and lower Manhattan have the highest trip densities, driven by commercial and tourist hotspots.
    2. **Regional Connectivity**: Significant travel links Manhattan to Jersey City and Brooklyn.
    3. **Key Hubs**: Certain stations dominate usage with trip counts >600, as shown by the color intensity.
    4. **Uneven Usage**: Northern Manhattan and peripheral areas show lower activity.
    5. **Focused Analysis**: Filters highlight high-demand routes and stations effectively.
    """)

# Conclusions and recommendations
else:
    st.header("Conclusions and recommendations")
    bikes = Image.open("/Users/ashwanisherawat/citibike_env/bin/Citi bike images/istockphoto-2181208335-612x612.jpg")
    st.image(bikes)
    st.markdown("### Our analysis has shown that Citi Bikes should focus on the following objectives moving forward:")
    st.markdown("- Add more stations to the locations around the water line, such as Theater on the Lake, Streeter Dr/Grand Avenue, Millenium Park, Columbus Dr/Randolph Street, Shedd Aquarium, Michigan Avenue/Oak Street, Canal Street/Adams Street.")
    st.markdown("- Ensure that bikes are fully stocked in all these stations during the warmer months in order to meet the higher demand, but provide a lower supply in winter and late autumn to reduce logistics costs.")


# In[ ]:




