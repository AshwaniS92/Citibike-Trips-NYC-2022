#!/usr/bin/env python
# coding: utf-8

# ## Imoprting Libraries

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from datetime import datetime as dt


# In[4]:


########################### Initial settings for the dashboard ##################################################################

st.set_page_config(page_title = 'Divvy Bikes Strategy Dashboard', layout='wide')
st.title("Divvy Bikes Strategy Dashboard")
st.markdown("The dashboard will help with the expansion problems Divvy currently faces")
st.markdown("Right now, Divvy bikes runs into a situation where customers complain about bikes not being avaibale at certain times. This analysis aims to look at the potential reasons behind this.")


# In[5]:


########################## Import data ###########################################################################################

# Path to the exported CSV file
file_path = '/Users/ashwanisherawat/citibike_env/bin/top20.csv'


# In[6]:


# Read the Pickle file into a DataFrame
top20 = pd.read_csv(file_path)


# In[7]:


top20.head(20)


# In[8]:


# Path to the exported CSV file
path = '/Users/ashwanisherawat/citibike_env/bin/debug_combined_df.csv'


# In[9]:


# Read the Pickle file into a DataFrame
combined_df = pd.read_csv(path)


# In[10]:


combined_df.head()


# In[11]:


## Bar chart

import plotly.graph_objects as go

fig = go.Figure(go.Bar(
    x=top20['value'],  # Sum of trips on x-axis
    y=top20['start_station_name'],  # Station names on y-axis
    orientation='h',  # Horizontal bar chart
    marker=dict(
        color=top20['value'],
        colorscale='Blues'
    )
))

fig.update_layout(
    title="Top 20 Most Popular Bike Stations in New York",
    xaxis_title="Sum of Trips",
    yaxis_title="Start Station",
    height=700,  # Increased height for better visibility
    width=800,   # Optional width adjustment
    margin=dict(l=100),  # Increase left margin to accommodate long station names
    yaxis=dict(tickangle=0, automargin=True)  # Ensure y-axis labels are fully visible
)

fig.show()
# Display the Plotly chart in Streamlit with full container width
st.plotly_chart(fig, use_container_width=True)


# In[12]:


## Line chart 

fig_2 = make_subplots(specs = [[{"secondary_y": True}]])
fig_2.add_trace(
    go.Scatter(
        x=combined_df['date'],
        y=combined_df['trip_count'],
        name='Daily Bike rides',
        marker=dict(color='blue')  # Fixed color to 'blue'
    ),
    secondary_y=False
)

fig_2.add_trace(
    go.Scatter(
        x=combined_df['date'],
        y=combined_df['Avg Temperature'],
        name='Daily Temperature',
        marker=dict(color='red')  # Fixed color to 'red'
    ),
    secondary_y=True
)
st.plotly_chart(fig_2, use_container_width=True)


# In[13]:


### Add the map ###

path_to_html = "/Users/ashwanisherawat/citibike_env/bin/Citi Bike Trips Aggregated.html" 

# Read file and keep in variable
with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
st.header("Aggregated Citi Bike Trips in New York")
st.components.v1.html(html_data,height=1000)


# In[ ]:




