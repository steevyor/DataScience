# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:56:56 2018

@author: sonia
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def loadDatas():
    #datas_file = pd.DataFrame.from_csv("spambase/spambase.data", header=0, sep=',', index_col=0);
    datas_file = pd.read_csv("spambase/spambase.data");
    return pd.DataFrame(datas_file)

def loadNames():
    datas_file = pd.read_csv("spambase/spambase.names");
    return pd.DataFrame(datas_file)

def colonne(nom):
    datas = loadDatas()
    return datas[nom]

datas = loadDatas()
names = loadNames()
print(names)

for name in names:
    print(datas[name])




x = colonne("make")
plt.plot(x, color = "blue")


plt.show()