import pandas as pd

# read the parquet file final_df.parquet
prediction = pd.read_parquet('final_df.parquet')

# Sort the dataframe by year, month, day, and hour
prediction = prediction.sort_values(by=['year', 'month', 'day', 'hour'])

# Add a timestamp column to the dataframe
prediction['timestamp'] = pd.to_datetime(prediction[['year', 'month', 'day']])

# Assign the day of the week to a new column
prediction['day_of_week'] = prediction['timestamp'].dt.day_name()

# For every month, group by day_of_week and print the average of docks_available per hour
prediction.groupby(['month', 'day_of_week', 'hour'])['docks_available'].mean().reset_index()

# Sort the dataframe by year, month, day, and hour
prediction = prediction.sort_values(by=['year', 'month', 'day', 'hour'])

# Export the prediction dataframe to a new parquet file
prediction.to_parquet('prediction_with_day_of_week.parquet', index=False)