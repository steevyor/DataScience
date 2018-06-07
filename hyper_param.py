# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:30:21 2018

@author: Henri
"""

import matplotlib.pyplot as plt

from collections import OrderedDict
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
RANDOM_STATE = 123
ensemble_clfs = [
    ("RandomForestClassifier, max_features='sqrt'",
        RandomForestClassifier(warm_start=True, oob_score=True,
                               max_features="sqrt",
                               random_state=RANDOM_STATE)),
    ("RandomForestClassifier, max_features='log2'",
        RandomForestClassifier(warm_start=True, max_features='log2',
                               oob_score=True,
                               random_state=RANDOM_STATE)),
    ("RandomForestClassifier, max_features=None",
        RandomForestClassifier(warm_start=True, max_features=None,
                               oob_score=True,
                               random_state=RANDOM_STATE))
]

# Map a classifier name to a list of (<n_estimators>, <error rate>) pairs.
error_rate = OrderedDict((label, []) for label, _ in ensemble_clfs)

# Range of `n_estimators` values to explore.
min_estimators = 10
max_estimators = 20


def hyper_param(x,y):
	for label, clf in ensemble_clfs:
    		for i in range(min_estimators, max_estimators + 1):
        		clf.set_params(n_estimators=i)
        		clf.fit(x, y)

        		# Record the OOB error for each `n_estimators=i` setting.
        		oob_error = 1 - clf.oob_score_
        		error_rate[label].append((i, oob_error))

	# Generate the "OOB error rate" vs. "n_estimators" plot.
	for label, clf_err in error_rate.items():
    		xs, ys = zip(*clf_err)
    		plt.plot(xs, ys, label=label)

plt.xlim(min_estimators, max_estimators)
plt.xlabel("n_estimators")
plt.ylabel("OOB error rate")
plt.legend(loc="upper right")
plt.show()