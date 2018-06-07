# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:17:06 2018

@author: sone-
"""

import load_data as ld
import matplotlib.pyplot as plt
import numpy as np



sup = ['label']
#sup = ['label', 'capital_average', 'capital_longest', 'capital_total']

datasColonnes = ld.loadDatas()
datas = datasColonnes.drop(columns = sup)
names = ld.loadNames()
names = names.drop(columns = sup)

moyennes = []
for name in names: 
    y = ld.colonne(name)
    m = ld.moyenneColonne(y)
    moyennes.append(m)
    
y = ld.colonne("make")
x = range(len(moyennes))
plt.bar(x, moyennes, 0.5, color="lightslategrey")
plt.figure(figsize = (50, 50))
plt.show()  
print("     Moyennes d'apparition de chaque mot")


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


#Graph spam ou non 
labels = ld.colonne("label")
count0 = 0
count1=0
for value in labels: 
    if value == 0:
        count0 = count0 + 1
    else:
        count1 = count1 + 1
        
        
y = [count0, count1]
x = np.arange(2)
plt.bar(x, y, 0.10,align='center', color="khaki")
plt.ylabel('Nombre de lignes')
plt.xticks(x, ('Non spam', 'Spam'))
plt.title('Répartition spam/non spam dans le datas set')
plt.axis([-0.1, 1.1, 0, 3000])
plt.show()
    
    
#Pour chaque mot, un graph
for name in names: 
    plt.plot((ld.colonne(name)))
    plt.show()
    print(name)

    
    
    