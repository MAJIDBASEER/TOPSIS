#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 


# In[2]:


# Data from chapter 5 - Topsis example 
mtx = [[690,3.1,9,7,4]
      ,[590,3.9,7,6,10]
      ,[620,3.8,7,10,6]
      ,[700,2.8,10,4,6]
      ,[650,4.0,6,9,8]]


# In[3]:


# Weight

w = [0.3,0.2,0.2,0.15,0.15]


# In[4]:


# Alternative names 
Names = ['Alfred','Beverly','Calvin','Diana','Edward']


# In[5]:


# Create dataframe
Data = pd.DataFrame(mtx, index = Names)
Data 


# In[6]:


# Step 1 - Normalization 
Data_norm = Data/np.sqrt(np.power(Data,2).sum(axis=0))


# In[7]:


np.sqrt(np.power(Data,2).sum(axis=0))


# In[8]:


Data_norm = Data/np.sqrt(np.power(Data,2).sum(axis=0))
Data_norm 


# In[9]:


# step 2 - Weighted normalized ratings 
Data_norm_w = Data_norm*w 
Data_norm_w


# In[10]:


# Step 3 - Identifying positive and negative ideals 
positive_ideal = Data_norm_w.max()
negative_ideal = Data_norm_w.min()


# In[11]:


negative_ideal = Data_norm_w.min()


# In[12]:


positive_ideal = Data_norm_w.max()


# In[13]:


# Step 4 - Separation Measurment:
# positive ideal
SM_P = np.sqrt(np.power(Data_norm_w-positive_ideal,2).sum(axis=1))
# Negative ideal 
SM_N = np.sqrt(np.power(Data_norm_w-negative_ideal,2).sum(axis=1))


# In[14]:


np.sqrt(np.power(Data_norm_w-positive_ideal,2).sum(axis=1))


# In[15]:


np.sqrt(np.power(Data_norm_w-negative_ideal,2).sum(axis=1))


# In[16]:


SM_N/(SM_N+SM_P)

