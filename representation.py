# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:17:06 2018

@author: sone-
"""

import load_data as ld
import matplotlib.pyplot as plt


datas = ld.loadDatas()
names = ld.loadNames()
print(names)

#for name in names:
#    print(datas[name])




y = ld.colonne("all")
print(y)
plt.plot(x, color = "blue")
plt.show()


N = len(y)
x = range(N)
plt.bar(x, y, 3, color="blue")
plt.show()