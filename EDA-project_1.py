#!/usr/bin/env python
# coding: utf-8

# ## The database is provided by UN Comtrade (a repository of official international trade statistics) for World Integrated Trade Solution (WITS) platform. Data points are collected from WITS iteratively (due to query limitations) and concatenated.
# 
# - Each observation constitutes export value of all goods from country i to country j in year t.df.loc[df['a'] == 1, 'b'].sum()

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('z-datasets/trade_1988_2021.csv')


# In[3]:


df


# In[4]:


df.info()


# In[5]:


df.describe()


# In[ ]:





# In[ ]:





# ## Exploratory Data Analysis (EDA)

# ### 1. Year

# In[6]:


import seaborn as sns
sns.set_style('darkgrid')


# In[7]:


df.Year


# In[8]:


U_year = df.Year.unique()
U_year


# In[9]:


len(U_year)


# In[10]:


year_by_trade = df.Year.value_counts()
year_by_trade


# In[11]:


year_by_trade.plot(kind = 'barh')


# In[12]:


sns.distplot(df.Year)


# In[13]:


high_year = year_by_trade[year_by_trade >= 20000]
low_year = year_by_trade[year_by_trade < 20000]


# In[14]:


len(low_year)


# In[15]:


sns.distplot(high_year)


# In[16]:


sns.distplot(low_year)


# In[ ]:





# In[ ]:





# In[ ]:





# ### 2. Trade Value

# In[17]:


trade_value_call = df['TradeValue in 1000 USD']
trade_value_call


# In[18]:


trade_values = trade_value_call.value_counts()
trade_values


# In[24]:


value_stats = df.groupby('Year')['TradeValue in 1000 USD'].sum()
value_stats


# In[25]:


value_stats.plot(kind = 'barh')


# In[23]:


sns.distplot(value_stats)


# In[ ]:




