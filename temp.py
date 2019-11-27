# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy.io as scio
import pandas as pd
import numpy as np
import xgboost
import sklearn
from sklearn.model_selection import train_test_split

dataFile = 'D:\sigh.mat'
data = scio.loadmat(dataFile)

data1=data['a3_1']
# =============================================================================
# print(data1.ndim)
# print(data1.shape)
# print(data1.dtype)
# print(data.keys())
# 
# import operator
# 
# from functools import reduce
# data2=reduce(operator.add, data1)
# =============================================================================
temp=data1[0][0][1]
data_last=temp[0:8000,:]
for i in range(1,2857):
    temp2=data1[0][i][1]
    b=temp2[0:8000,:]
    data_last=np.column_stack((data_last,b))
data_last=data_last.transpose()

target=data1[0][0][3]
target=target[:,0]
for j in range(1,2857):
    target1=data1[0][j][3]
    target2=target1[:,0]
    target=np.row_stack((target,target2))
#print(target)

train_X,test_X, train_y, test_y = train_test_split(data_last,target,test_size = 0.3,random_state = 0)
Boost_Model = xgboost.XGBClassifier().fit(train_X, train_y)
Accuracy = sklearn.metrics.accuracy_score(test_y, Boost_Model.predict(test_X))
print("Accuracy: %.2f" % Accuracy)

print("Feature Important: \n")
b=Boost_Model.feature_importances_
print(b)



