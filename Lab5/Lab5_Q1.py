#!/usr/bin/env python
# coding: utf-8

# In[223]:


#import statements
import pandas as pd
import numpy as np


# In[224]:

# ### Question 1 Time Series Data Practice

# import Energy.xlsx to pandas dataframe
df = pd.read_excel(r'Energy.xlsx')
print(df.shape)  # check if data is imported correctly by checking dimensions


# In[225]:


# getting column index by column name
index_1 = df.columns.get_loc("Accumulated Other Comprehensive Income (Loss)")
index_2 = df.columns.get_loc("Selling, General and Administrative Expenses")


# In[226]:


# function definition for splitEnergy
def splitEnergy(StartYear=2012, EndYear=None):
    df_temp = df

    # set column 'Data Date' type to string to split year and convert back to integer
    df_temp['Data Date'] = df_temp['Data Date'].astype(str).str[:4].astype(int)

    # If EndYear is None, we will only choose all data with ”Data Date” == StartYear as Test data, all other data as Train data.
    # By default, all company Data Date within 2012 will be selected as Testing data.
    if (EndYear == None):
        TestData = df_temp[df_temp['Data Date'] == StartYear]
        TrainData = df_temp[df_temp['Data Date'] != StartYear]

    # If EndYear is NOT None, we will choose all data with ”Data Date” == StartYear to EndYear as Test data, all other data as Train data
    else:
        TestData = df_temp[(df_temp['Data Date'] >= StartYear)
                           & (df_temp['Data Date'] <= EndYear)]
        TrainData = df_temp[(df_temp['Data Date'] < StartYear)
                            | (df_temp['Data Date'] > EndYear)]

    # array from column ”Accumulated Other Comprehensive Income (Loss)” to column ”Selling, General and Administrative Expenses”.
    TestData = TestData.iloc[:, index_1:index_2]
    TrainData = TrainData.iloc[:, index_1:index_2]

    # Output Data type: Array(Numpy)
    return TestData.values, TrainData.values


# In[227]:


# function execution
splitEnergy(2012, 2013)


# In[ ]:
