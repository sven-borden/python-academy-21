from math import * 
import numpy as np
import matplotlib.pyplot as plt


def listecarre(x):
    carre = [] 
    for i in x:
        j = i*i
        carre.append(j)
    return carre

carre = listecarre([4, 2, 3, 4])

print(carre)


def listeracine(x):
    racine = []
    for i in x:
        j = sqrt(i)
        racine.append(j)
    return racine


racine = listeracine([4, 16, 9])

print(racine)


def liste_cos_sin(x):

    coss = []
    for i in x:
        a = radians(i)
        j = cos(a)
       
        coss.append(j)
    
    sinn = []
    for w in x:
        z = radians(w)
        l = sin(z)
       
        sinn.append(l)

    return coss, sinn

x = range(1000)

coss, sinn = liste_cos_sin(x)

print(coss)

print(sinn)
'''
crée la figure
'''
plt.figure()
'''
introduction des valeurs x et y
'''
'''
introduit une légende 
'''
plt.plot(x, coss,'--b', label = 'cosinus')
plt.plot(x, sinn, 'g', label = 'sinus')
'''
permet de titrer les axes
'''
plt.xlabel('angles en °')
plt.ylabel('cos/sin')
''''
déplace l'endroit ou la légende est ércite
'''
plt.legend(loc = "lower right")

''''
affiche le graphique
'''
plt.show()









