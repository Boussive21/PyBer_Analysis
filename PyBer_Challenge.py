#!/usr/bin/env python
# coding: utf-8

# # Pyber Challenge

# ### 4.3 Loading and Reading CSV files

# In[156]:


# Add Matplotlib inline magic command
get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd

# File to Load (Remember to change these)
city_data_to_load = "city_data.csv"
ride_data_to_load = "ride_data.csv"

# Read the City and Ride Data
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)


# In[157]:


# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the data table for preview
pyber_data_df.head()


# ### Merge the DataFrames

# ## Deliverable 1: Get a Summary DataFrame 

# In[158]:


#  1. Get the total rides for each city type

total_rides_by_type = pyber_data_df.groupby(["type"]).count()["ride_id"]

total_rides_by_type


# In[159]:


# 2. Get the total drivers for each city type
total_drivers_by_type = city_data_df.groupby(["type"]).sum()["driver_count"]
total_drivers_by_type


# In[160]:


#  3. Get the total amount of fares for each city type
total_fares_by_type = pyber_data_df.groupby(["type"]).sum()["fare"]

total_fares_by_type


# In[161]:


#  4. Get the average fare per ride for each city type. 
avg_ridefare =  total_fares / total_rides

avg_ridefare


# In[162]:


# 5. Get the average fare per driver for each city type. 
avg_driverfare =  total_fares / total_drivers

avg_driverfare


# In[163]:


#  6. Create a PyBer summary DataFrame. 
pyber_summary_df = pd.DataFrame({
    "Total Rides": total_rides_by_type,
    "Total Drivers": total_drivers_by_type,
    "Total Fares": total_fares_by_type,
    "Average Fare per Ride": avg_ridefare,
    "Average Fare per Driver": avg_driverfare})

pyber_summary_df


# In[164]:


#  7. Cleaning up the DataFrame. Delete the index name
pyber_summary_df.index.name = None


# In[165]:


#  8. Format the columns.
pyber_summary_df["Total Rides"] = pyber_summary_df["Total Rides"].map("{:,}".format)
pyber_summary_df["Total Drivers"] = pyber_summary_df["Total Drivers"].map("{:,}".format)
pyber_summary_df["Total Fares"] = pyber_summary_df["Total Fares"].map("${:,.2f}".format)
pyber_summary_df["Average Fare per Ride"] = pyber_summary_df["Average Fare per Ride"].map("${:.2f}".format)
pyber_summary_df["Average Fare per Driver"] = pyber_summary_df["Average Fare per Driver"].map("${:.2f}".format)

# Display the data frame
pyber_summary_df


# ## Deliverable 2.  Create a multiple line plot that shows the total weekly of the fares for each type of city.

# In[166]:


# 1. Read the merged DataFrame
pyber_data_df.head()


# In[167]:


# 2. Using groupby() to create a new DataFrame showing the sum of the fares 
#  for each date where the indices are the city type and date.
fare_by_city_date_df = pyber_data_df.groupby(['type','date']).sum().fare.to_frame()
fare_by_city_date_df.head(5)


# In[168]:


# 3. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.
# df = df.reset_index()
fare_by_city_date_df = fare_by_city_date_df.reset_index()
fare_by_city_date_df.head(5)


# In[169]:


# 4. Create a pivot table with the 'date' as the index, the columns ='type', and values='fare' 
# to get the total fares for each type of city by the date. 
fare_by_city_date_df = fare_by_city_date_df.pivot(index='date',columns='type', values='fare')
fare_by_city_date_df.head(5)


# In[170]:


# 5. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.
fare_dates_df = fare_by_city_date_df.loc['2019-01-01':'2019-04-29']
fare_dates_df


# In[171]:


# 6. Set the "date" index to datetime datatype. This is necessary to use the resample() method in Step 8.
# df.index = pd.to_datetime(df.index)
type(fare_dates_df.index)

fare_dates_df.index = pd.to_datetime(fare_dates_df.index)
fare_dates_df.head()


# In[172]:


# 7. Check that the datatype for the index is datetime using df.info()
fare_dates_df.info()


# In[173]:


# 8. Create a new DataFrame using the "resample()" function by week 'W' and get the sum of the fares for each week.
fare_dates_df = fare_dates_df.resample('W').sum()
fare_dates_df


# In[177]:


# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function. 

# Import the style from Matplotlib.
from matplotlib import style
# Use the graph style fivethirtyeight.
style.use('fivethirtyeight')
fare_dates_df.plot(figsize=(25,10),)
plt.xlabel('')
plt.ylabel('Fare ($USD)')
plt.title('Total Fare by City Type')
plt.savefig('analysis/Pyber_fare_summary.png');


# In[ ]:





# In[ ]:




