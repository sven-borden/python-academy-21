import random

def fonction(x, liste1):
    liste2 = []
    for i in liste1:
        if i < x:
            liste2.append(i)
    return liste2



       
def gener_liste():
    liste3 = []
 
    for i in range(random.randrange(2,20)):
        n = random.randrange(1,100)
        liste3.append(n)

    return liste3   

n = gener_liste()

y = input()
x = float(y)

liste_final = fonction(x, n)
 
print (liste_final)

print (n)













