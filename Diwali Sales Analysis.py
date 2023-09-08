#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import seaborn as sns


# In[4]:


df = pd.read_csv('Diwali Sales Data.csv', encoding = 'unicode escape')


# In[5]:


df


# In[6]:


df.head(60)


# In[7]:


df.info()


# In[8]:


df.drop(['Status', 'unnamed1'], axis = 1, inplace = True)


# In[9]:


df


# In[10]:


pd.isnull(df)


# In[11]:


pd.isnull(df).sum()


# In[12]:


df.dropna(inplace = True)


# In[13]:


pd.isnull(df).sum()


# In[14]:


df['Amount'] = df['Amount']. astype(int)


# In[15]:


df['Amount'].dtypes


# In[16]:


df.rename( columns = {'Marital_Status': 'Shaadi'}, inplace = True)


# In[17]:


df


# In[18]:


df.describe()


# In[19]:


df[['Age', 'Amount', 'Orders']].describe()


# # DATA ANALYSIS

# ## Gender

# In[20]:


ax = sns.countplot( x = 'Gender', data = df)


# In[21]:


ax = sns.countplot( x = 'Gender', data = df, label = False)


# In[ ]:




