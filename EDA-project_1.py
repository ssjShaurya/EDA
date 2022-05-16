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





# ## Observations for Year and Trade Value
# ### -Year
# - As seen above trade over the years can be catagorized in two broad groups i.e. high_year and low_year
#   
#   -High Year
#   - high_year has more than or equal to 20000 volume traded
#   - for 20000 to 217000 density of numbers of years is high
#   - but 21700 and 23000 density decreases
#   - once we reache 23000 volume traded density increases again
#   This suggests that trade has been going pretty good as a high density of years have volume traded greater than 23000
#  
#   -Low Year
#   - low_year has less than 20000 volume traded
#   - 5000 to 15000 volume traded has about the ame density i.e. about equal number of years
#   - whereas a geater number of years have more than 15000 teaded in vaolume
#    This suggest that more and more years were begining to incounter good fortune in relation to volume traded
#    
#  ### - Trade Value
#  - Trade Value is taken to be the sum of mone made through trade in one year (for scale 10 million will be treated as 1)
#    - over the years profit made has steadily increased with some exceptions
#    - for 0 to 2 the density is extremely high suggesting it was the satrting of trade and every year trade was getting better
#    - for 2 to 3 the density drops suggesting this much amount was made over a lesser number of years
#    - according to the bar-graph its between this time period (2008 - 2016) that we saw major fluctuations clueing us to the fact that trade was quite unstable for some time
#    - after 3.5 the profit began to rise again till 2020 when it fell again, trend continuing into 2021

# In[ ]:




