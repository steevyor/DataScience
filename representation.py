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

for name in names:
    print(datas[name])




x = ld.colonne("make")
plt.plot(x, color = "blue")


plt.show()