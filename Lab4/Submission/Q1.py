#!/usr/bin/env python
# coding: utf-8

# ## Q1. Credit Transaction data(40 points)

# This dataset is simulated individual credit card transactions by one company. Please use this dataset to answer following question. Please notice that you may need to observe the dataset and clean it before answering the following question.

# In[51]:


# --> Import statements
import pandas as pd
import re


# In[52]:


df = pd.read_csv("res_purchase_2014.csv", low_memory=False) #importing dataset res_purchase_2014.csv
print(df.head()) #displaying top 5 rows


# ### 1. What is total amount spending captured in this dataset?
# Hint: you may observe $ in front of the amount, which you need remove it (see.row 12), and () stands for negative value, which you need deduct the amount.

# In[50]:


df = df.dropna() #dropping NA values 
new = []
for value in df['Amount']:
    if(type(value) == str):
        value = value.strip()
        
        if(value[0] == '(' and value[-1] == ')'):
            value = str('-' + value[1:-1]) #if value contains () 
            
        if('$' in value): 
            value = value.replace('$', '') #if value contains $
            
        if(re.search('[a-zA-Z]', value)): 
            value = re.sub('[a-zA-Z]', '', value) #if value contains words
            
        value = float(value.strip()) #strip whitespace and convert str to float 
        
    new.append(value)
df['Amount'] =  new


# In[41]:


total = df['Amount'].sum() #sum all values 
print("Total Amount spent:",round(total,2)) #round to 2 digit


# ### 2. How much was spend at WW GRAINGER?
# Hint: All ‘WW GRAINGER’ contained in the ‘Vendor’.

# In[42]:


count = 0
for i in range(len(df)): 
    if(df['Vendor'][i] == 'WW GRAINGER'): #check for vendor with value WW GRAINGER 
        count = count + df['Amount'][i] #if found then add to count


# In[43]:


print("Total Amount spent at WW GRAINGER:",round(count,2)) #round to 2 digit


# ### 3. How much was spend at WM SUPERCENTER?
# Hint: All ‘WM SUPERCENTER’ contained in the ‘Vendor’.
# 

# In[44]:


count_sc = 0
for i in range(len(df)): 
    if(df['Vendor'][i] == 'WM SUPERCENTER'): #check for vendor with value WM SUPERCENTER
        count_sc = count_sc + df['Amount'][i] #if found then add to count


# In[45]:


print("Total Amount spent at WM SUPERCENTER:",round(count_sc,2))  #round to 2 digit


# ### 4. How much was spend at GROCERY STORES?
# Hint: All ‘GROCERY STORES’ contained in the ‘Merchant Category Code’.

# In[46]:


count_gc = 0
for i in range(len(df)): 
    if('GROCERY STORES' in df['Merchant Category Code (MCC)'][i] ): #check for MCC with value GROCERY STORES
        count_gc = count_gc + df['Amount'][i]


# In[47]:


print("Total Amount spent at GROCERY STORES:",round(count_gc,2)) #round to 2 digit


# ### Final Output

# In[49]:


print('Results for Part 1: \n _________________\n')
print("Total Amount spent:",round(total,2)) #round to 2 digit
print("Total Amount spent at WW GRAINGER:",round(count,2)) #round to 2 digit
print("Total Amount spent at WM SUPERCENTER:",round(count_sc,2))  #round to 2 digit
print("Total Amount spent at GROCERY STORES:",round(count_gc,2)) #round to 2 digit


# In[ ]:




