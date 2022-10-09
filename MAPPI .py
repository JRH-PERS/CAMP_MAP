#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium


# In[2]:


import pandas as pd


# In[3]:


marker1 = pd.read_csv('map2.csv')


# In[4]:


marker1.head()


# In[5]:


marker1.info()


# In[6]:


mapp = folium.Map(
)


for index, row in marker1.iterrows():
    iframe = folium.IFrame('NAME:' + str(row.loc['NAME:']) + '<br>' + '<br>' + 'ABOUT: ' + row.loc['ABOUT:'] + '<br>' + '<br>' +'RATING: ' + str(row.loc['RATING:']))
    popup = folium.Popup(iframe, min_width=300, max_width=300)
    folium.Marker(location=[row.loc['latitude'], row.loc['longitude']], icon=folium.Icon(color=row.loc['colour'], icon='map-marker', prefix='fa'), popup=popup).add_to(mapp)


# In[7]:


mapp


# In[8]:


mapp.save('my_maps.html')


# In[ ]:





# In[ ]:




