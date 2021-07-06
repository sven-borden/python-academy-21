'''
eip = est il premier
'''
eip = True111


a = input()
a = int(a)
b = range(2,a)


for i in b:
    d = a % i 
    if d == 0: 
        eip = False


if eip == False:
    print('non premier')
else:
    print('premier')
























