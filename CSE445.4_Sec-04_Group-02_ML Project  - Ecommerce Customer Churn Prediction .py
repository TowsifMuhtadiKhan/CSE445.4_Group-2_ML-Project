#!/usr/bin/env python
# coding: utf-8

# __Importing Important Python Libraries__

# In[2]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import sklearn as skl 


# In[3]:


df = pd.read_excel('E-Commerce_Dataset.xlsx')
df


# In[4]:


df.info(verbose=True)


# In[5]:


df.isnull()


# In[6]:


df.shape


# In[7]:


df.head(10)


# In[8]:


df.describe(include='all')


# In[10]:


#Find the duplicates

df.duplicated().sum()


# In[13]:


print(df.Churn.value_counts())


# In[9]:


ax=sns.countplot(x='Churn', data = df)


# In[14]:


print(df.Gender.value_counts())


# In[15]:


ax=sns.countplot(x='Gender', data = df)


# In[16]:


print(df.SatisfactionScore.value_counts())


# In[17]:


ax=sns.countplot(x='SatisfactionScore', data = df)

