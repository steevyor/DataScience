# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 15:56:56 2018

@author: sonia
"""
import pandas as pd


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

def moyenneColonne(colonne):  
    return colonne.mean()
        
