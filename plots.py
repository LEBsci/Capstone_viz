import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

prediction = pd.read_parquet('prediction_with_day_of_week.parquet')

# Create a new column called bikes_available
prediction['bikes_available'] = 1 - prediction['docks_available']

# Take the data for station_id 92, on wednesdays
df1 = prediction[(prediction['station_id'] == 230) & (prediction['day_of_week'] == 'Wednesday') & (prediction['month'] > 5)]

# average bikes available per hour for every tuesday in 2023
year_one = df1[df1['year'] == 2022].groupby(['hour'])['bikes_available'].mean().reset_index()

# Plot the average bikes available per hour for every tuesday in 2022

plt.figure(0, figsize=(12, 6))
sns.lineplot(data=year_one, x='hour', y='bikes_available', label='2022')

year_two = df1[df1['year'] == 2023].groupby(['hour'])['bikes_available'].mean().reset_index()

# Plot the average bikes available per hour for every tuesday in 2023
# plt.figure(figsize=(12, 6))
sns.lineplot(data=year_two, x='hour', y='bikes_available', label='2023')

year_three = df1[df1['year'] == 2024].groupby(['hour'])['bikes_available'].mean().reset_index()
# plt.figure(figsize=(12, 6))
sns.lineplot(data=year_three, x='hour', y='bikes_available', label='2024')

plt.xticks(rotation=45)
plt.xlabel('Hour of the Day')
plt.ylabel('Average Bikes Available')
plt.xticks(range(0, 24), rotation=45)
plt.grid()
plt.tight_layout()
plt.title('Average Bikes Available per Hour for Wednesdays in station 230, June to December')
plt.legend(title='Year')


plt.savefig('average_bikes_available_per_hour_wednesdays_230.png', dpi=300, bbox_inches='tight')




# Take the data for station_id 92, on wednesdays
df2 = prediction[(prediction['station_id'] == 230) & (prediction['day_of_week'] == 'Saturday') & (prediction['month'] > 5)]

# average bikes available per hour for every tuesday in 2023
year_one = df2[df2['year'] == 2022].groupby(['hour'])['bikes_available'].mean().reset_index()

# Plot the average bikes available per hour for every tuesday in 2022
plt.figure(1, figsize=(12, 6))
sns.lineplot(data=year_one, x='hour', y='bikes_available', label='2022')

year_two = df2[df2['year'] == 2023].groupby(['hour'])['bikes_available'].mean().reset_index()

# Plot the average bikes available per hour for every tuesday in 2023
# plt.figure(figsize=(12, 6))
sns.lineplot(data=year_two, x='hour', y='bikes_available', label='2023')

year_three = df2[df2['year'] == 2024].groupby(['hour'])['bikes_available'].mean().reset_index()
# plt.figure(figsize=(12, 6))
sns.lineplot(data=year_three, x='hour', y='bikes_available', label='2024')

plt.xticks(rotation=45)
plt.xlabel('Hour of the Day')
plt.ylabel('Average Bikes Available')
plt.xticks(range(0, 24), rotation=45)
plt.grid()
plt.tight_layout()
plt.title('Average Bikes Available per Hour for Saturdays in station 230, June to December')
plt.legend(title='Year')

plt.savefig('average_bikes_available_per_hour_saturdays_230.png', dpi=300, bbox_inches='tight')


# Make a plot for the average bikes available depending on the rain
plt.figure(2, figsize=(12, 6))
sns.lineplot(data=df1, x='relative_humidity_2m', y='bikes_available')
plt.xlabel('relavtive_humidity_2m')
plt.ylabel('Average Bikes Available')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.title('Average Bikes Available per Rain')
plt.savefig('average_bikes_available_per_humidity.png', dpi=300, bbox_inches='tight')

plt.show()