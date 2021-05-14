import pandas as pd
import numpy as np 
from numpy import vstack
import matplotlib.pyplot as plt

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.linear_model import LinearRegression

from math import sqrt

import pickle

from pickle import dump

df = pd.read_csv('auto_final.csv') 

target = df[['mpg']] 
predictors = df[['cylinders','displacement','horsepower','weight','acceleration','year','originL']]

X = predictors.values
y = target.values

sc2 = StandardScaler()
X = sc2.fit_transform(X)
dump(sc2, open('scaler.pkl', 'wb'))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)
print(X_train.shape); 
print(X_test.shape)

reg = LinearRegression().fit(X,y)
reg

filename = 'model.sav'
pickle.dump(reg, open(filename, 'wb'))
