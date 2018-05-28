# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:48:07 2018

@author: Henri
"""

#Here are the different imports for the cross validation:

#from sklearn.model_selection import cross_val_score
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split as tts
#from sklearn.model_selection import train_test_split as tts

#Here are our different SKLEARN Classifiers imports:

from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.base import BaseEstimator 
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import neighbors, datasets
from sklearn.neighbors import KNeighborsClassifier

import numpy as np
from process import process
import pickle
RANDOM_STATE = 123


class Classifier(RandomForestClassifier):
    def __init__(self):
        pass

    def fit(self, X, y):
        pro = process(X, y)
        a = pro.getFeatures()
        b = pro.getLabels()
        self.clf = RandomForestClassifier(n_jobs = -1, n_estimators = 100, warm_start=True, max_features=None,
                               oob_score=True,
                               random_state= RANDOM_STATE)
        self.clf.fit(a, b)

    def predict(self, X):
	X = process(X)
        return self.clf.predict(X)

    def predict_proba(self, X):
	X = process(X)
        return self.clf.predict_proba(X) # The classes are in the order of the labels returned by get_classes
        
    def get_classes(self):
        return self.clf.classes_
        
    def save(self, path="./"):
        pickle.dump(self, open(path + '_model.pickle', "w"))

    def load(self, path="./"):
        self = pickle.load(open(path + '_model.pickle'))
        return self


    def  best_fit(self,names, classifiers, x, y):
	
        pro = process(x, y)
        a = pro.getFeatures()
        b = pro.getLabels()

    	score_boucle_train = []
    	final_array = []
    	best=["",0]

    	for name, clf in zip(names, classifiers):
        	score_boucle_train.append( cross_val_score(clf, a, b, cv=10, n_jobs=1 ))

    	final_array=np.mean(score_boucle_train, axis=1, dtype=np.float64) 

    	for score, name in zip(final_array, names):
        
        	if score>best[1] :
            		best[1]=score
            		best[0]=name
    	return best

	
    def  return_final_array(self,names, classifiers, x, y):
	
        pro = process(x, y)
        a = pro.getFeatures()
        b = pro.getLabels()

    	score_boucle_train = []
    	final_array = []
  	best=["",0]

    	for name, clf in zip(names, classifiers):
        	score_boucle_train.append( cross_val_score(clf, a, b, cv=10, n_jobs=1 ))

    	final_array=np.mean(score_boucle_train, axis=1, dtype=np.float64) 
	return final_array








