# -*- coding: utf-8 -*-
"""Vijay Bhasin

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/vijaybasic/a9a5d1110870d2666bade4f4d5aab00c/untitled5.ipynb
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import os
import seaborn as sns

df = pd.read_csv('/content/weight-height.csv')
df

df.isnull().sum()

X = df.iloc[:, 1:2].values
y = df.iloc[:, 2:3].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=31)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

model_fit = regressor.fit(X_train, y_train)

y_predict = regressor.predict(X_test)

y_predict

plt.scatter(X_test, y_test)
plt.plot( X_train, regressor.predict(X_train), color='r')
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Heigth Vs Weight Prediction")
plt.show()

from sklearn.metrics import r2_score

print(f"Model Accuracy is: {regressor.score(X_test, y_test)}")

r2_score(y_test, y_predict)

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import os
import seaborn as sns

df1 = pd.read_csv('/content/weight-height.csv')
df1

df.isnull().sum()

X_ml = df.iloc[:, 1:3].values
y_ml = df.iloc[:, 0:1].values

X_ml.shape

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

y_ml = encoder.fit_transform(y_ml)

y_ml

y_ml.shape

X_train_ml, X_test_ml, y_train_ml, y_test_ml = train_test_split(X_ml, y_ml, test_size=0.3, random_state=31)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train_ml, y_train_ml)

y_predict_ml = knn.predict(X_test_ml)
y_predict_ml

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test_ml, y_predict_ml)

knn = KNeighborsClassifier(n_neighbors=5) 
knn.fit(X_train_ml, y_train_ml)
y_predict_ml = knn.predict(X_test_ml)
cm = confusion_matrix(y_test_ml, y_predict_ml)
cm

print("accuracy:", knn.score(X_test_ml, y_test_ml))