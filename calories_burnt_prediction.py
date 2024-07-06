# -*- coding: utf-8 -*-
"""Calories Burnt Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1184hkTa_v2lEA0Pw0Pg36dtjnTNCxfOQ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

calories = pd.read_csv('/content/calories.csv')

calories.head()

exercise_data = pd.read_csv('/content/exercise.csv')

exercise_data.head()

# combaining the two dataframes
calories_data = pd.concat([exercise_data,calories['Calories']],axis=1)

calories_data.head()

calories_data.shape

calories_data.info()

calories_data.isnull().sum()

calories_data.describe()

sns.set()

sns.countplot(x=calories_data['Gender'])

sns.displot(calories_data['Age'])

sns.displot(calories_data['Height'])

sns.displot(calories_data['Weight'])

calories_data.replace({"Gender":{'male':0,'female':1}}, inplace=True)

correlation = calories_data.corr()

plt.figure(figsize=(10,10))
sns.heatmap(correlation,cbar=True,square=True,fmt='.1f',annot=True)

calories_data.head()

X = calories_data.drop(columns=['User_ID','Calories'],axis=1)
Y = calories_data['Calories']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

model = XGBRegressor()

model.fit(X_train,Y_train)

test_data_prediction = model.predict(X_test)

mae = metrics.mean_absolute_error(Y_test,test_data_prediction)

print("Mean Absolute Error= ",mae)

