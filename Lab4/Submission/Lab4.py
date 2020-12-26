
#!/usr/bin/env python
# coding: utf-8


# ## Q1. Credit Transaction data(40 points)

# This dataset is simulated individual credit card transactions by one company. Please use this dataset to answer following question. Please notice that you may need to observe the dataset and clean it before answering the following question.

# In[51]:


# --> Import statements
import pandas as pd
import re
import numpy as np


# In[52]:

print('###########')
print('Question 1')
print('###########')

# importing dataset res_purchase_2014.csv
df = pd.read_csv("res_purchase_2014.csv", low_memory=False)
print('\nDisplay first 5 rows of dataframe:\n')
print(df.head())  # displaying top 5 rows


# ### 1. What is total amount spending captured in this dataset?
# Hint: you may observe $ in front of the amount, which you need remove it (see.row 12), and () stands for negative value, which you need deduct the amount.

# In[50]:


df = df.dropna()  # dropping NA values
new = []
for value in df['Amount']:
    if(type(value) == str):
        value = value.strip()

        if(value[0] == '(' and value[-1] == ')'):
            value = str('-' + value[1:-1])  # if value contains ()

        if('$' in value):
            value = value.replace('$', '')  # if value contains $

        if(re.search('[a-zA-Z]', value)):
            value = re.sub('[a-zA-Z]', '', value)  # if value contains words

        # strip whitespace and convert str to float
        value = float(value.strip())

    new.append(value)
df['Amount'] = new


# In[41]:


total = df['Amount'].sum()  # sum all values
print("Total Amount spent:", round(total, 2))  # round to 2 digit


# ### 2. How much was spend at WW GRAINGER?
# Hint: All ‘WW GRAINGER’ contained in the ‘Vendor’.

# In[42]:


count = 0
for i in range(len(df)):
    if(df['Vendor'][i] == 'WW GRAINGER'):  # check for vendor with value WW GRAINGER
        count = count + df['Amount'][i]  # if found then add to count


# In[43]:


print("Total Amount spent at WW GRAINGER:",
      round(count, 2))  # round to 2 digit


# ### 3. How much was spend at WM SUPERCENTER?
# Hint: All ‘WM SUPERCENTER’ contained in the ‘Vendor’.
#

# In[44]:


count_sc = 0
for i in range(len(df)):
    if(df['Vendor'][i] == 'WM SUPERCENTER'):  # check for vendor with value WM SUPERCENTER
        count_sc = count_sc + df['Amount'][i]  # if found then add to count


# In[45]:


print("Total Amount spent at WM SUPERCENTER:",
      round(count_sc, 2))  # round to 2 digit


# ### 4. How much was spend at GROCERY STORES?
# Hint: All ‘GROCERY STORES’ contained in the ‘Merchant Category Code’.

# In[46]:


count_gc = 0
for i in range(len(df)):
    # check for MCC with value GROCERY STORES
    if('GROCERY STORES' in df['Merchant Category Code (MCC)'][i]):
        count_gc = count_gc + df['Amount'][i]


# In[47]:


print("Total Amount spent at GROCERY STORES:",
      round(count_gc, 2))  # round to 2 digit


# ### Final Output

# In[49]:

print('\n####### FINAL ANSWER FOR QUESTION 1 ########')

print('Results for Part 1: \n _________________\n')
print("Total Amount spent:", round(total, 2))  # round to 2 digit
print("Total Amount spent at WW GRAINGER:",
      round(count, 2))  # round to 2 digit
print("Total Amount spent at WM SUPERCENTER:",
      round(count_sc, 2))  # round to 2 digit
print("Total Amount spent at GROCERY STORES:",
      round(count_gc, 2))  # round to 2 digit


# In[ ]:

#######################################

#!/usr/bin/env python
# coding: utf-8

# ## Q2 Data Processing with Pandas (60 points)
# In this practice, you are expected to play around Pandas and get familiar with it. The dataset is quarterly dataset downloading from WRDS. Please remember that you need to do data transformation based on the new dataset generated by previous step. Do not using other package other than numpy and pandas.

# In[261]:


# --> Import statements


# ### 1. Read’Energy.xlsx’and’EnergyRating.xlsx’as BalanceSheet and Ratings(dataframe)

# In[262]:

print('\n###########')
print('Question 2')
print('###########\n')
BalanceSheet = pd.read_excel("Energy.xlsx")  # importing dataset Energy.csv
print('Q1. Display first 5 rows of BalanceSheet: \n')
print(BalanceSheet.head())  # displaying top 5 rows


# In[263]:


# importing dataset EnergyRating.csv
Ratings = pd.read_excel("EnergyRating.xlsx")
print('\nQ1. Display first 5 rows of Ratings: \n')
print(Ratings.head())  # displaying top 5 rows


# ### 2. drop the column if more than 90% value in this colnmn is 0 (or missing value).

# In[264]:


def dropColumn(df):
    delList = []
    df = df.fillna(value=np.nan)
    for column in df.columns:
        # check if value in column is 0 or null or NaN then add
        if(((df[column] == 0).sum() + df[column].isnull().sum() + df[column].isna().sum())/len(df) > 0.9):
            delList.append(column)
    return delList


print('\nQ2. Size of Dataframes before dropping:')
print('BalanceSheet:', BalanceSheet.shape)
print('Ratings:', Ratings.shape)
print("-------------------")

# drop columns with more than 90% 0 or null values
BalanceSheet = BalanceSheet.drop(columns=dropColumn(BalanceSheet))
Ratings = Ratings.drop(columns=dropColumn(Ratings))

print('Size of Dataframes after dropping:')
print('BalanceSheet:', BalanceSheet.shape)
print('Ratings:', Ratings.shape)


# ### 3. replace all None or NaN with average value of each column.

# In[269]:


BalanceSheet = BalanceSheet.fillna(value=BalanceSheet.mean())
Ratings = Ratings.fillna(value=Ratings.mean())


# ### 4. Normalize the table (Only need to normalize numerical parts)

# In[270]:


def normalize(df):
    num_cols = list(df.columns[df.dtypes.apply(
        lambda c: np.issubdtype(c, np.number))])
    for col in num_cols:
        df[col].apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
    return df


BalanceSheet = normalize(BalanceSheet)
Ratings = normalize(Ratings)


# ### 5. Define an apply function to return the statistical information for variables = [’Current Assets - Other - Total’, ’Current Assets - Total’, ’Other Long-term Assets’, ’Assets Netting & Other Adjustments’], you need to return a dataframe which has exactly same format with pandas method .describe().
#

# In[280]:


index = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
column_names = ["Current Assets - Other - Total", "Current Assets - Total",
                "Other Long-term Assets", "Assets Netting & Other Adjustments"]

df = pd.DataFrame(columns=column_names, index=index)


# In[282]:


def res(column):
    data = [len(column), column.mean(), column.std(),
            column.min()]  # calculate data points
    q1, q2, q3 = column.quantile([.25, .5, .75]).to_list()
    data += [q1, q2, q3, column.max()]
    return data


temp = BalanceSheet[column_names].apply(res, axis=0)  # calling res function
for i in df.columns:
    df[i] = temp[i]  # adding back to dataframe

print(
    '\nQ5. Statistical information for variables = [’Current Assets - Other - Total’, ’Current Assets - Total’, ’Other Long-term Assets’, ’Assets Netting & Other Adjustments’]: \n')
print(df)


# ### 6. Calculate the correlation matrix for variables = [’Current Assets - Other - Total’, ’Current Assets - Total’, ’Other Long-term Assets’, ’Assets Netting & Other Adjustments’].

# In[273]:


correlation = BalanceSheet[column_names].corr()
print('\nQ6 Correlation: \n')
print(correlation)


# ### 7. If you look at column (’Company Name’), you will find some company name end with ’CORP’, ’CO’ or ’INC’. Create a new column (Name: ’CO’) to store the last word of company name. (For example: ’CORP’ or, ’CO’ or ’INC’) (Hint: using map function)

# In[274]:


BalanceSheet["CO"] = BalanceSheet["Company Name"].map(lambda x: x.split()[-1])


# In[279]:

print('\nQ7. Splitting company name to new column `CO`\n')
print(BalanceSheet)


# ### 8. Merge (inner) Ratings and BalanceSheet based on ’datadate’ and ’Global Com- pany Key’, and name merged dataset ’Matched’.

# In[275]:


Matched = pd.merge(Ratings, BalanceSheet, how="inner",
                   on=["Data Date", "Global Company Key"])
print('\nQ8. Merging Ratings and BalanceSheet based on ’datadate’ and ’Global Company Key’\n')
print(Matched.head())


# ### 9. Mapping
# For dataset ’Matched’, we have following mapping: AAA = 0
# AA+ = 1
# AA = 2
#  AA- =3 A+ = 4 A=5
# A- = 6 BBB+ = 7
# 2
# BBB = 8
# BBB- = 9
# BB+ = 10
# BB = 11
# others = 12
# Using map function to create a new varible = ’Rate’, which maps ratings to numerical ratings.

# In[276]:


ratings = {"AAA": 0, "AA+": 1, "AA": 2, "AA-": 3, "A+": 4, "A": 5,
           "A-": 6, "BBB+": 7, "BBB": 8, "BBB-": 9, "BB+": 10, "BB": 11}
Matched["Rate"] = Matched['S&P Domestic Long Term Issuer Credit Rating'].map(
    lambda x: ratings.get(x, 12))


# In[277]:

print('\nQ9. Dataframe with new column `Rate` to map ratings to numeric value\n')
print(Matched.head())


# ### 10. Calculate the rating frequency of company whose name end with ’CO’. (Calcu- late the distribution of rating given the company name ending with ’CO’, Hint, use map function)

# In[278]:


freq = Matched[Matched["CO"] == "CO"]["Rate"].value_counts() / \
    len(Matched[Matched["CO"] == "CO"])
print("\nQ10. Frequency counts:\n")
print(freq)


# In[ ]: