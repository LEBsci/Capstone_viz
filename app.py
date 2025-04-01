import pandas as pd
import streamlit as st
import plotly.express as px

# Cache the loading of the dataset
@st.cache_data
def load_data():
    return pd.read_parquet('final_df.parquet')

# Load the dataset
prediction = load_data()

# Static UI elements
st.title("Animated Maps of Locations")
col1, col2, col3 = st.columns(3)
with col1:
    year = st.selectbox("Select Year", sorted(prediction['year'].unique()))
with col2:
    month = st.selectbox("Select Month", sorted(prediction['month'].unique()))
with col3:
    day = st.selectbox("Select Day", sorted(prediction['day'].unique()))

# Filter the DataFrame based on the selected year, month, and day
@st.cache_data
def filter_data_for_animation(prediction, year, month, day):
    return prediction[
        (prediction['year'] == year) &
        (prediction['month'] == month) &
        (prediction['day'] == day)
    ]

filtered_df = filter_data_for_animation(prediction, year, month, day)
# Sort the DataFrame by hour for consistent animation
filtered_df = filtered_df.sort_values(by='hour')

# Create an animated map using Plotly
st.subheader(f"Hourly Animation for {year}-{month}-{day}")

fig = px.scatter_map(
    filtered_df,
    lat="lat",
    lon="lon",
    color="docks_available",  # Color intensity based on docks_available
    color_continuous_scale="Turbo",  # Color scale
    range_color=(0, 1),  # Keep the color scale between 0 and 1
    size_max=20,  # Maximum size of the points
    zoom=10,  # Initial zoom level
    animation_frame="hour",  # Animate by hour
    title=f"Hourly Changes in Locations for {year}-{month}-{day}",
    map_style="carto-positron",  # Use OpenStreetMap

)

fig.update_traces(marker=dict(size=7))  # Set size to 7 (adjust as needed)

# Update the layout to position the color scale legend at the bottom
fig.update_layout(
    height=800,  # Set the height of the map
    coloraxis_colorbar=dict(
        orientation="h",  # Horizontal orientation
        x=0.5,  # Center the legend horizontally
        xanchor="center",  # Anchor the legend at the center
        y=1.0,  # Position the legend below the map
        title="Docks Available",  # Add a title to the color scale
    )
)

# Display the animated map in Streamlit
st.plotly_chart(fig)

# Import the prediction_with_day_of_week.parquet file
@st.cache_data
def load_prediction_with_day_of_week():
    return pd.read_parquet('prediction_with_day_of_week.parquet')

day_prediction = load_prediction_with_day_of_week()
# Filter the DataFrame based on the selected year, month, and day of the week
col1, col2, col3 = st.columns(3)
with col1:
    year = st.selectbox("Select Year", sorted(day_prediction['year'].unique()), key="year_day_of_week")
with col2:
    month = st.selectbox("Select Month", sorted(day_prediction['month'].unique()), key="month_day_of_week")
with col3:
    day_of_week = st.selectbox("Select Day of Week", sorted(day_prediction['day_of_week'].unique()), key="day_of_week")

# Filter the DataFrame based on the selected year, month, and day of the week
@st.cache_data
def filter_data_by_day_of_week(day_prediction, year, month, day_of_week):
    return day_prediction[
        (day_prediction['year'] == year) &
        (day_prediction['month'] == month) &
        (day_prediction['day_of_week'] == day_of_week)
    ]

filtered_day_df = filter_data_by_day_of_week(day_prediction, year, month, day_of_week)
# Sort the DataFrame by hour for consistent animation
filtered_day_df = filtered_day_df.sort_values(by='hour')
# Create an animated map using Plotly

st.subheader(f"Hourly Animation for {year}-{month} on {day_of_week}s")
fig = px.scatter_map(
    filtered_day_df,
    lat="lat",
    lon="lon",
    color="docks_available",  # Color intensity based on docks_available
    color_continuous_scale="Turbo",  # Color scale
    range_color=(0, 1),  # Keep the color scale between 0 and 1
    size_max=20,  # Maximum size of the points
    zoom=10,  # Initial zoom level
    animation_frame="hour",  # Animate by hour
    title=f"Hourly Changes in Locations for {year}-{month} on {day_of_week}",
    map_style="carto-positron",  # Use OpenStreetMap

)

fig.update_traces(marker=dict(size=7))  # Set size to 7 (adjust as needed)

# Update the layout to position the color scale legend at the bottom
fig.update_layout(
    height=800,  # Set the height of the map
    coloraxis_colorbar=dict(
        orientation="h",  # Horizontal orientation
        x=0.5,  # Center the legend horizontally
        xanchor="center",  # Anchor the legend at the center
        y=1.0,  # Position the legend below the map
        title="Docks Available",  # Add a title to the color scale
    )
)
# Display the animated map in Streamlit
st.plotly_chart(fig)