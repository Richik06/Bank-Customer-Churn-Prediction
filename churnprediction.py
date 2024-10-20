# -*- coding: utf-8 -*-
"""ChurnPrediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kMVSzEdKAR26IgEx45AZi9qAX2T_OkK3
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

churn="/content/archive (1).zip"
dataset=pd.read_csv(churn)

dataset.head()

dataset.tail()

dataset['Geography'].unique()

dataset=pd.get_dummies(data=dataset,drop_first=True)

dataset

dataset.Exited.plot.hist()

#people staying with the company
(dataset.Exited==0).sum()

#people exited from company
(dataset.Exited==1).sum()

dataset_2=dataset.drop(columns='Exited')

dataset_2.corrwith(dataset['Exited']).plot.bar(figsize=(16,9), title='Correlated with Exited Column', rot = 45,grid = True)

corr=dataset.corr()

plt.figure(figsize=(16,9))
sns.heatmap(corr,annot=True)

X= dataset.drop(columns='Exited')
y= dataset['Exited']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

X_train.shape

X_test.shape

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train= scaler.fit_transform(X_train)
X_test= scaler.transform(X_test)

X_train

# Logistic regression is used for predicting the categorical dependent variable using a given set of independent variables.
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=0).fit(X_train, y_train)

y_pred= clf.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score

acc=accuracy_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)
prec=precision_score(y_test,y_pred)
rec=recall_score(y_test,y_pred)

results=pd.DataFrame([['Logistic regression',acc,f1,prec,rec]],columns=['Model','Accuracy','F1','Precision','Recall'])
results

print(confusion_matrix(y_test,y_pred))

#Random Forest is a classifier that contains a number of decision trees on various subsets of the given dataset and it takes the average to improve the predictive accuracy of that dataset.
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0).fit(X_train, y_train)
y_pred= clf.predict(X_test)
acc=accuracy_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)
prec=precision_score(y_test,y_pred)
rec=recall_score(y_test,y_pred)
RF_results=pd.DataFrame([['Random Forest Classifier',acc,f1,prec,rec]],columns=['Model','Accuracy','F1','Precision','Recall'])
results = pd.concat([results, RF_results], ignore_index=True)
results

print(confusion_matrix(y_test,y_pred))

dataset.head()

# Entering random data to predict whether customer will churn or not
single_obs=[[647,40,3,85000.45,2,0,0,92012.45,0,1,1]]
clf.predict(scaler.fit_transform(single_obs))

# at above array is 0 which means customer is going to stay with the bank