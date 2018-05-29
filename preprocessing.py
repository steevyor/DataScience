# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:27:56 2018

@author: Henri
"""

import load_data as ld
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def buildDataSet():
    datas = ld.loadDatas()
    datas = datas.drop( columns =['label'])
    return datas



def divide(x, y):
    X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size = 0.2, random_state = 42)
    print(X_train, X_test, Y_train, Y_test)
    return X_train, X_test, Y_train, Y_test
    
def buildTargets():
    return ld.colonne('label')

def preprocess(datas):
    scaler = StandardScaler().fit(datas)
    return scaler.transform(datas)