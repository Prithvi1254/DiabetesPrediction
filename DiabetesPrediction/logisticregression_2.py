# -*- coding: utf-8 -*-
"""logisticRegression 2.ipynb

"""

#import libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
# to create plots bar, histogram, boxplot etc
import seaborn as sns
import matplotlib.pyplot as plt
# calculate accuracy measure and confusion matrix from sklearn import metrics
from sklearn import metrics
# Load CSV file
Data= pd.read_csv("/content/diabetes.csv")
from sklearn.preprocessing import StandardScaler

from google.colab import drive
drive.mount('/content/drive')

Data.head().transpose()

Data.dtypes

Data.describe ()

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X= Data.drop("Outcome", axis=1)
y= Data[["Outcome"]]
X_train, X_test, y_train, y_test=train_test_split( X,y,test_size=0.10, random_state=7)

model = LogisticRegression()
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
model_score = model.score (X_test, y_test)

print(model_score)
print(metrics.confusion_matrix(y_test,y_predict))

input_data= (4,110,92,0,0,37.6,0.191,30)

# changing the input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = model.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not Diabetic')

else:
  print('The person is Diabetic')
