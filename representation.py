# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:17:06 2018

@author: sone-
"""

import load_data as ld
import matplotlib.pyplot as plt



sup = ['label', 'capital_average', 'capital_longest', 'capital_total']
datas = ld.loadDatas()
datas = datas.drop(columns = sup)
names = ld.loadNames()
names = names.drop(columns = sup)

print(datas)
print(names)

moyennes = []
for name in names: 
    y = ld.colonne(name)
    m = ld.moyenneColonne(y)
    moyennes.append(m)
    
#print(moyennes)
    
    
y = ld.colonne("make")
x = range(len(moyennes))
plt.bar(x, moyennes, 0.5, color="lightslategrey")
plt.show()  

max1 = 0
max2 = 0
max3 = 0
max4 = 0
max5 = 0
max6 = 0
max7 = 0
max8 = 0
max9 = 0
max10 = 0

label1 = ""
label2 = ""
label3 = ""
label4 = ""
label5 = ""
label6 = ""
label7 = ""
label8 = ""
label9 = ""
label10 = ""

moyennesLabels = {"moyenne":[], "label":[]}
for name in names: 
    y = ld.colonne(name)
    m = ld.moyenneColonne(y)
    moyennesLabels["moyenne"].append(m)
    moyennesLabels["label"].append(name)
print(moyennesLabels)

for moyenne in moyennesLabels["moyenne"]:
    if moyenne > max1:
        max1 = moyenne
    elif moyenne > max2:
        max2 = moyenne
    elif moyenne > max3:
        max3 = moyenne
    elif moyenne > max4:
        max4 = moyenne
    elif moyenne > max5:
        max5 = moyenne
    elif moyenne > max6:
        max6 = moyenne
    elif moyenne > max7:
        max7 = moyenne
    elif moyenne > max8:
        max8 = moyenne
    elif moyenne > max9:
        max9 = moyenne
    elif moyenne > max10:
        max10 = moyenne
  
        

        
        

    
    
    
    
    