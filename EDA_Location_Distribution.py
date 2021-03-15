#!/usr/bin/env python
# coding: utf-8

# ## < EDA : Location Distribution >
# 
# We would like to see where the geographical distribution of Air BNB rentals in NYC and find out where the popular locations are as well.

# In[1]:


# Import packages

import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[3]:


# Load dataset

df = pd.read_csv("~/Desktop/AirBnbNYC2019.csv") 
df.head()


# In[4]:


# Identify variable types

def describe_data(df):
    print("Data Types:")
    print(df.dtypes)
    print("Rows and Columns:")
    print(df.shape)
    
describe_data(df)


# In[5]:


# Identify column names for further analysis
 
list(df.columns)


# In[6]:


# Identify unique borough names

df['neighbourhood_group'].unique()


# In[7]:


# Create an interactive distribution map for AirBNB locations in NYC.

import pandas as pd
import folium

m1 = folium.Map(location=[40.693943, -73.985880], default_zoom_start=10, width=640, height=480)

for lat, lon, label in zip(df.latitude, df.longitude, df.neighbourhood.astype(str)):
    if label!='0':
        folium.features.CircleMarker(
            [lat, lon],
            radius=0.1,
            color='#0f4fff',
            color_opacity=0.6
        ).add_to(m1)

m1


# In[8]:


# Check location frequencies for each boroughs

BoroCounts = df.neighbourhood_group.value_counts()
print("-------Frequency counts for BORO column-------\n",BoroCounts)
print(type(BoroCounts))


# In[9]:


# Connstruct a pie chart for above summary

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

counts = pd.Series([44.3, 41.1, 11.6, 2.2, 0.8], 
                   index=['Manhattan (44.3%)', 'Brooklyn (41.1%)', 'Queens (11.6%)', 
                          'Bronx (2.2%)', 'Staten Island (0.8%)'])

explode = (0,0,0.1,0.2,0.3)
colors = ['#666666', '#911818', '#f4db1a', '#23079c', '#347a06']

counts.plot(kind='pie', fontsize=12, colors=colors, explode=explode)
plt.axis('equal')
plt.ylabel('')
plt.show()


# < Location destribution summary >
# - Airbnb locations in NYC are mostly in Manhattan and Brooklyn: detailed distribution is below;
#     1. Manhattan = 44.3% (21661 listings)
#     2. Brooklyn = 41.1% (20104 listings)
#     3. Queens = 11.6% (5666 listings)
#     4. Bronx = 2.2% (1091 listings)
#     5. Staten Island = 0.8% (373 listings)
