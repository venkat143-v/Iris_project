# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:52:33 2023

@author: Lenovo
"""



import pandas as pd
import numpy as np

data=pd.read_csv(r"C:\Users\Lenovo\Desktop\python\DriveReady\ML\iris.csv")

data.shape
data.size
data.head()
data.info()
data.describe()

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(
    x,y,test_size=0.2,random_state=9)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=1)
model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)

print(model.predict([[5.4,3.9,1.7,0.4]]))
