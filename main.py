# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:57:19 2018

@author: Henri
"""

import load_data as ld
import preprocessing as pp
import classifier
import matplotlib.pyplot as plt
import hyper_param as hp
import numpy as np

#function made to create barchart
def histocomparaison(valeurs,categories):
    plt.bar(range(len(valeurs)), valeurs,align="center",alpha=.5)
    plt.xticks(range(len(valeurs)), categories,rotation=90,fontsize=10)
    plt.show()
    
    


x = pp.preprocess(pp.buildDataSet())
y = pp.buildTargets()

#splitted data      
X_train, X_test, Y_train, Y_test = pp.divide(x,y)

names = ["RandomForest", "KNeighbors", "DecisionTree", "GaussianNB", 
         "AdaBoostClassifier"]
         
classifiers = [ classifier.RandomForestClassifier(), 
                classifier.KNeighborsClassifier(), 
                classifier.DecisionTreeClassifier(),
                classifier.GaussianNB(),
                classifier.AdaBoostClassifier()
                ]

c = classifier.Classifier()

print(c.best_fit(names, classifiers, X_train, Y_train))

#fit and predict a simple randomForestClassifier
clf = classifier.RandomForestClassifier()
clf.fit(X_train, Y_train)
clf.predict(X_test)
print(clf.score(X_test, Y_test))

#Displays the performance differences between the selected algorythms
# Multiple classifiers have been removed to keep our representation readable
# and not overload user's CPU
histocomparaison(c.return_final_array(names, classifiers, x, y),names)

#We fit and predict on our data set with a tuned RandomForestClassifier
clfBest = classifier.RandomForestClassifier(n_jobs = -1, n_estimators = 1000, warm_start=True, max_features=2,
                               oob_score=True,
                               random_state= hp.RANDOM_STATE)

clfBest.fit(X_train, Y_train)
print(clfBest.score(X_test, Y_test))

#We call the hyper_param function from the hyper_param class. It will show the differences between 3 tuning
#setups of randomForest hyper parameters. 
hp.hyper_param(x,y)
                               