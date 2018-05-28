# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:27:56 2018

@author: Henri
"""

import numpy as np
import pandas as pd
import load_data as ld
from sklearn.preprocessing import StandardScaler

def buildDataSet():
    datas = ld.loadDatas()
    return datas.drop(columns = ['label'])
    
def buildTargets():
    return ld.colonne('label')

def preprocess(datas):
    scaler = StandardScaler().fit(datas)
    return scaler.transform(datas)