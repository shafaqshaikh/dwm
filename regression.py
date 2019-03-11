# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


#importimg dataset

dataset=pd.read_csv('Salary_Data.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values


#splitting the dataset into the training and test sets
from sklearn.model_selection import train_test_split


X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=1/3,random_state=0)




from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train, y_train)


y_pred=regressor.predict(X_test)




plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('salary vs Experience (Training set)')
plt.x.label('years of Experience')
plt.ylabel('salary')
plt.show()



plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('salary vs Experience (Test set)')
plt.x.label('years of Experience')
plt.ylabel('salary')
plt.show()













