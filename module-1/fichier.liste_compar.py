import random

def compar(liste1, liste2):
    liste3 = [] 
    for i in liste1:
        for v in liste2:
            if v == i:
                liste3.append(v)
    return liste3

def gener_liste():
    liste3 = []
 
    for i in range(random.randrange(2,20)):
        n = random.randrange(1,100)
        liste3.append(n)

    return liste3  


liste1 = gener_liste()

liste2 = gener_liste()

liste3 = gener_liste()

liste_final = compar(liste1, liste2)

print(liste1)

print(liste2)

print (liste_final)

liste_vrm_final = compar(liste3,liste_final)

print(liste3)

print(liste_vrm_final)

mega_liste = []

for e in range (3):
    l = gener_liste()
    
    mega_liste.append(l)

u_1 = range(1,99)

print(mega_liste)

for u in mega_liste:

    u_1 = compar(u,u_1)



print(u_1)










