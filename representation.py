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
'''
moyennes = []
for name in names: 
    y = ld.colonne(name)
    m = ld.moyenneColonne(y)
    moyennes.append(m)
    
y = ld.colonne("make")
x = range(len(moyennes))
plt.bar(x, moyennes, 0.5, color="lightslategrey")
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

for i in range(len(moyennesLabels["moyenne"])):
    if moyennesLabels["moyenne"][i] > max1:
        max1 = moyennesLabels["moyenne"][i]
        label1 = moyennesLabels["label"][i]
    elif moyennesLabels["moyenne"][i] > max2:
        max2 = moyennesLabels["moyenne"][i]
        label2 = moyennesLabels["label"][i]
    elif moyennesLabels["moyenne"][i] > max3:
        max3 = moyennesLabels["moyenne"][i]
        label3 = moyennesLabels["label"][i]
    elif moyennesLabels["moyenne"][i] > max4:
        max4 = moyennesLabels["moyenne"][i]
        label4 = moyennesLabels["label"][i]
    elif moyennesLabels["moyenne"][i] > max5:
        max5 = moyennesLabels["moyenne"][i]
        label5 = moyennesLabels["label"][i]
    elif moyennesLabels["moyenne"][i] > max6:
        max6 = moyennesLabels["moyenne"][i]
        label6 = moyennesLabels["label"][i]
    elif moyennesLabels["moyenne"][i] > max7:
        max7 = moyennesLabels["moyenne"][i]
        label7 = moyennesLabels["label"][i]
    elif moyennesLabels["moyenne"][i] > max8:
        max8 = moyennesLabels["moyenne"][i]
        label8 = moyennesLabels["label"][i]
    elif moyennesLabels["moyenne"][i] > max9:
        max9 = moyennesLabels["moyenne"][i]
        label9 = moyennesLabels["label"][i]
    elif moyennesLabels["moyenne"][i] > max10:
        max10 = moyennesLabels["moyenne"][i]
        label10 = moyennesLabels["label"][i]
  
        
        

plt.plot((ld.colonne(label1)))
plt.show()  
print("     Fréquences d'apparition pour : ", label1)
plt.plot((ld.colonne(label2)))
plt.show()  
print("     Fréquences d'apparition pour : ", label2)
plt.plot((ld.colonne(label3)))
plt.show()  
print("     Fréquences d'apparition pour : ", label3)
plt.plot((ld.colonne(label4)))
plt.show()  
print("     Fréquences d'apparition pour : ", label4)
plt.plot((ld.colonne(label5)))
plt.show() 
print("     Fréquences d'apparition pour : ", label5)
plt.plot((ld.colonne(label6)))
plt.show()  
print("     Fréquences d'apparition pour : ", label6)
plt.plot((ld.colonne(label7)))
plt.show()  
print("     Fréquences d'apparition pour : ", label7)
plt.plot((ld.colonne(label8)))
plt.show()  
print("     Fréquences d'apparition pour : ", label8)
plt.plot((ld.colonne(label9)))
plt.show()  
print("     Fréquences d'apparition pour : ", label9)
plt.plot((ld.colonne(label10)))
plt.show()  
print("     Fréquences d'apparition pour : ", label10)


'''

 

N = 50
x = datas['']
print(x)
y = ld.loadDatas()['label']
print(y)
#colors = np.random.rand(N)
#area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, alpha=0.5)
plt.show()

        

    
    
    
    
    