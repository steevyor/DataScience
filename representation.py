# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:17:06 2018

@author: sone-
"""

import load_data as ld
import matplotlib.pyplot as plt
import numpy as np


#Suppression des colonnes à décommenter selon les graphiques
sup = ['label', 'capital_average', 'capital_longest', 'capital_total']
#sup = ['label']

#Chargement des données
datasColonnes = ld.loadDatas()
datas = datasColonnes.drop(columns = sup)
names = ld.loadNames()
names = names.drop(columns = sup)

#Génération des moyennes par mot
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


moyennesLabels = {"moyenne":[], "label":[]}
for name in names: 
    y = ld.colonne(name)
    m = ld.moyenneColonne(y)
    moyennesLabels["moyenne"].append(m)
    moyennesLabels["label"].append(name)
    print(m, " ", name)


#Graph de la rfréquence d'apparition en fonction du numéro de ligne
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
    
    
#Pour chaque mot, un graph de fréquence en fonction de la ligne
for name in names: 
    plt.plot((ld.colonne(name)))
    plt.show()
    print(name)


#Performances en enlevant des colonnes
y = [0.9543, 0.9576, 0.9587, 0.9554, 0.9565, 0.9565]
x = np.arange(6)
plt.bar(x, y, 0.80,align='center', color="yellowgreen")
plt.ylabel('Performances')
plt.xticks(x, ('0.9543 ', '0.9576', '0.9587', '0.9554 ', '0.9565', '0.9565' )) 
plt.title('Evolution des performances de notre classifier en fonction des données')
plt.show()
    


#Performances en faisant varier cross validation et hyper parametres
y = [0.9418, 0.9551, 0.96 , 0.9446]
x = np.arange(4)
plt.bar(x, y, 0.40,align='center', color="yellowgreen")
plt.ylabel('Performances')
plt.xticks(x, ('RF cv sans hp', 'RF cv avec hp', 'RF n cv avec hp', 'RF n cv sans hp' )) 
plt.title('Evolution des performances de notre classifier en fonction de la cross validation et des hyper paramètres')
plt.show()
    
    