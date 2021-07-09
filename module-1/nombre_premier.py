'''
eip = est il premier
'''

def nombre_premier(a):
    
    eip = True

    b = range(2,a)

    for i in b:
        d = a % i 
        if d == 0: 
            eip = False
    return eip


a = input()
a = int(a)
c = range(2,a)

for i in c:
    estpremier = nombre_premier(i)
    if estpremier == True:
        print (i)






