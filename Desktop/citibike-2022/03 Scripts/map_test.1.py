#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from datetime import datetime as dt


# In[2]:


########################### Initial settings for the dashboard ##################################################################

st.set_page_config(page_title = 'Citi Bikes Strategy Dashboard', layout='wide')
st.title("Citi Bikes Strategy Dashboard")
st.markdown("The dashboard will help with the expansion problems Citi currently faces")
st.markdown("Right now, Citi bikes runs into a situation where customers complain about bikes not being avaibale at certain times. This analysis aims to look at the potential reasons behind this.")


# In[3]:


# Direct download link from Google Drive
# url = "https://drive.google.com/file/d/1rXJyKWqirMTHvJBcg2fB2M5a-wNHq0TV/view?usp=sharing"

# Fetch the HTML file content
# response = requests.get(url)

# if response.status_code == 200:
  #   st.components.v1.html(response.text, height=700)
# else:
   #  st.error("Failed to load the HTML file. Please try again later.")


# In[4]:


# Raw GitHub link to the HTML file
github_html_url = "https://raw.githubusercontent.com/AshwaniS92/citibike-trips-nyc-2022/master/Desktop/citibike-2022/03%20Scripts/Citi%20Bike%20Trips%20Aggregated.html"

# Fetch the HTML content from GitHub
response = requests.get(github_html_url)

if response.status_code == 200:
    st.components.v1.html(response.text, height=700)
else:
    st.error("Failed to load the HTML file. Please check the link or try again later.")


# In[ ]:




