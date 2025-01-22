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

########################## Import data ###########################
# Path to the exported CSV file
file_path = f"{os.getcwd()}/top20.csv"
path = f"{os.getcwd()}/debug_combined_df.csv"

# Read the data files
top20 = pd.read_csv(file_path)
df = pd.read_csv(path)

# Generate all column names
column_names = df.columns
print("Column names:")
for col in column_names:
    print(col)

########################### Initial settings ######################

st.set_page_config(page_title='Citi Bikes Strategy Dashboard', layout='wide')
st.title("Citi Bikes Strategy Dashboard")

# Define side bar
st.sidebar.title("Aspect Selector")
page = st.sidebar.selectbox('Select an aspect of the analysis',
    ["Intro page", "Weather component and bike usage",
     "Most popular stations",
     "Interactive map with aggregated bike trips", "Recommendations"])

# Intro page
if page == "Intro page":
    st.markdown("#### This dashboard aims at providing helpful insights on the expansion problems Citi Bikes currently faces.")
    st.markdown("Right now, Citi bikes runs into a situation where customers complain about bikes not being available at certain times. This analysis will look at the potential reasons behind this. The dashboard is separated into 4 sections:")
    st.markdown("- Most popular stations")
    st.markdown("- Weather component and bike usage")
    st.markdown("- Interactive map with aggregated bike trips")
    st.markdown("- Recommendations")
    st.markdown("The dropdown menu on the left 'Aspect Selector' will take you to the different aspects of the analysis our team looked at.")

    try:
        myImage = Image.open("istockphoto-2190292731-612x612.jpg")
        st.image(myImage, caption="Citi Bike Image")
    except FileNotFoundError:
        st.error("Image not found: istockphoto-2190292731-612x612.jpg")

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

# Most popular stations
elif page == "Most popular stations":
    total_rides = float(top20['value'].sum())
    st.metric(label='Total Bike Rides', value=numerize(total_rides))

    top20 = top20.nlargest(20, 'value')
    fig = go.Figure(
        go.Bar(
            x=top20['value'],
            y=top20['start_station_name'],
            orientation='h',
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

    path_to_html = "Citi Bike Trips Aggregated_50000.html"
    try:
        with open(path_to_html, 'r') as f:
            html_data = f.read()

        st.header("Aggregated Bike Trips in New York")
        st.components.v1.html(html_data, height=1000)
    except FileNotFoundError:
        st.error(f"HTML file not found: {path_to_html}")

    st.markdown("#### Using the filter on the left-hand side of the map we can check whether the most popular start stations also appear in the most popular trips.")
    st.markdown("### Key Observations:")
    st.markdown("""
    1. **High Activity in Manhattan**: Central and lower Manhattan have the highest trip densities, driven by commercial and tourist hotspots.
    2. **Regional Connectivity**: Significant travel links Manhattan to Jersey City and Brooklyn.
    3. **Key Hubs**: Certain stations dominate usage with trip counts >600, as shown by the color intensity.
    4. **Uneven Usage**: Northern Manhattan and peripheral areas show lower activity.
    5. **Focused Analysis**: Filters highlight high-demand routes and stations effectively.
    """)

# Recommendations
else:
    st.header("Conclusions and recommendations")
    try:
        bikes = Image.open("istockphoto-2181208335-612x612.jpg")
        st.image(bikes, caption="Citi Bike Recommendations Image")
    except FileNotFoundError:
        st.error("Image not found: istockphoto-2181208335-612x612.jpg")
        st.markdown("### Our analysis highlights key factors contributing to bike shortages and uneven usage patterns across Citi Bike stations:")
    st.markdown("""
    1. **Seasonal Variability**: Bike usage peaks during warmer months (May–October) and drops significantly in colder months, driven by temperature variations. This seasonal demand surge likely leads to complaints about bike unavailability.
    2. **High-Demand Stations**: Specific stations in central and lower Manhattan, such as W 21 St & 6 Ave, West St & Chambers St, and Broadway & W 58 St, dominate usage. However, this high concentration of activity creates imbalances in supply and demand.
    3. **Uneven Regional Activity**: Peripheral areas, such as northern Manhattan and some outer boroughs, show lower activity, indicating underutilization of resources.
    4. **Regional Connectivity**: Significant travel links between Manhattan, Jersey City, and Brooklyn emphasize the need for better infrastructure and bike management across these hubs.
    5. **Redistribution Gaps**: Current operational strategies may not sufficiently address the variability in demand, especially during peak seasons and at high-traffic stations.
    """)
