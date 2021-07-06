a = 1
b = 3
if (a == 1) or (b == 3):
    print('oui')
else:
    print('non')

if (a == 1) and (b == 3):
    print('oui')
else:
    print('non')


def fa(x):
    print(f'{x}+{x}-{x}')
    a = input()
    b = float(a)
    '''
    float converti une chaine de caractère en nombre a virgule
    '''
    c = str(b)
    '''
    inverse de float
    '''

    print(type(b))
    if (b != x):
        print(f'faux, la valeurs est pas égale {b}')
    else: 
        print('juste')

fa(2)
fa(1)
x = [9, 4, 0, 5, 3]
second = x[1]
print(len(x))

x.append(6)

x.sort(reverse=True)
print(x)








print(x[5])

a = 8
b = 7
c = a + b 

d = a - b

e = a / b

f = a * b

g = a % 2  # g = 0

h = b % 2  # h = 1

"""
% -> divise sans les nombres à virgules et garde le surplus
"""







