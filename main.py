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

#print(c.best_fit(names, classifiers, X_train, Y_train))

#fit, ptrdict
clf = classifier.RandomForestClassifier()
clf.fit(X_train, Y_train)
clf.predict(X_test)
print(clf.score(X_test, Y_test))

#histocomparaison(c.return_final_array(names, classifiers, x, y),names)


clfBest = classifier.RandomForestClassifier(n_jobs = -1, n_estimators = 1000, warm_start=True, max_features=2,
                               oob_score=True,
                               random_state= hp.RANDOM_STATE)

clfBest.fit(X_train, Y_train)
print(clfBest.score(X_test, Y_test))
                               
                               
#x = np.delete(x, (0), axis=0)
#y = np.delete(y, (0), axis=0)

#TrainingX = SplitX[0]
#PredictX = SplitX[1]
#
#TrainingY = SplitY[0]
#PredictY = SplitY[1]
#
#clf.fit(TrainingX, TrainingY)
#
#prediction = clf.predict(PredictX)
#print(clf.score(prediction, PredictY))


#PredictY
#
#
#clf.fit(x,y)
#print(clf.score(x,y))

