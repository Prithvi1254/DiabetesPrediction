# -*- coding: utf-8 -*-
"""MachineLearninggprojSVM (2).ipynb


"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""DATA COLLECTION

PIMA DATABASE(only of females)
"""

diabetes_dataset = pd.read_csv('/content/diabetes.csv')

"""PRINTING THE FIRST 5 ROW OF DIABETES HERE 1 INDICATES DIABITIC PATIENT AND 0 INDICATES NON DIABITIC"""

diabetes_dataset.head()

diabetes_dataset.shape

diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

diabetes_dataset.groupby('Outcome').mean()

X=diabetes_dataset.drop(columns='Outcome',axis=1)
Y=diabetes_dataset['Outcome']

print(X)

print(Y)

"""DATA STADARDARIZATION"""

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

"""Train Test Split"""

X_train , X_test , Y_train , Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape,X_test.shape)

"""Training the Model"""

classifier = svm.SVC(kernel= 'linear')

classifier.fit(X_train, Y_train)

# accuracy score on the training data

X_train_prediction= classifier.predict(X_train)
training_data_accuracy= accuracy_score (X_train_prediction,Y_train)



print('Accuracy score of training data :',training_data_accuracy)

# accuracy score on the test data

X_test_prediction= classifier.predict(X_test)
test_data_accuracy= accuracy_score (X_test_prediction,Y_test)

print('Accuracy score of test data :',test_data_accuracy)

"""SVM"""

input_data= (4,110,92,0,0,37.6,0.191,30)

# changing the input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
  print('The person is not Diabetic')

else:
  print('The person is Diabetic')
