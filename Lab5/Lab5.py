#!/usr/bin/env python
# coding: utf-8

# ### import statements

# In[18]:


import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from pprint import pprint


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

# ### Question 3 Regression

# #### 3.1 & 3.2

# In[19]:


# Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Split the data into training/testing sets
# Split the targets into training/testing sets

diabetes_X_train, diabetes_X_test, diabetes_y_train, diabetes_y_test = train_test_split(
    diabetes_X, diabetes_y, test_size=0.20, random_state=42)


# #### 3.3

# In[20]:


# Create linear regression object
linreg = linear_model.LinearRegression()

# Train the model using the training sets
linreg.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = linreg.predict(diabetes_X_test)


# In[21]:


# The coefficients
print('Coefficients: \n', linreg.coef_)

# The coefficient of determination: 1 is perfect prediction
print('\nR-squared score: %.2f'
      % r2_score(diabetes_y_test, diabetes_y_pred))


# #### 3.4

# In[22]:


# Using 10-fold cross validation to fit and validate linear regression models on the whole data set. Printing the scores for each validation.

scores = cross_val_score(linreg, diabetes_X_train, diabetes_y_train, cv=10)
count = 1
for i in scores:
    print("Cross Validation Score for fold ", count, "is: ", i)
    count = count + 1

print("\nMean Accuracy: %0.2f with STD DEVIATION:  %0.2f" %
      (np.mean(np.abs(scores)), scores.std() * 2))


# #### 3.5

# In[26]:


# Use sklearn to create RandomForestRegressor model, and fit the training data into it.

rforest = RandomForestRegressor(
    n_estimators=1000, max_depth=None, min_samples_split=2, random_state=1)
rforest.fit(diabetes_X_train, diabetes_y_train)

diabetes_y_pred = rforest.predict(diabetes_X_test)
# calculating the r square score
print('\nR-squared score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# calculating root mean sq error
print("Root mean squared test error = {0}".format(
    np.sqrt(np.mean((rforest.predict(diabetes_X_test) - diabetes_y_test)**2))))


# #### 3.6

# In[24]:


# Using Grid Search to find the optimal hyper-parameters

# setup randomforest
rforest = RandomForestRegressor(
    n_estimators=1000, max_depth=None, min_samples_split=2, random_state=1)

# setup and train GridSearchCV
clf = GridSearchCV(
    rforest, {'max_depth': [None, 7, 4], 'min_samples_split': [2, 10, 20]}, cv=10)
model = clf.fit(diabetes_X_train, diabetes_y_train)

# print optimal hyper-parameters
pprint(model.best_estimator_.get_params())


# In[25]:


# print R-squared score
diabetes_y_pred = model.predict(diabetes_X_test)
print('\nR-squared score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))
