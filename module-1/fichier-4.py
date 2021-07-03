
print('entres la valeur de la longeur du paralèlépipède réctangle ?')
a = input()
b = float(a)

print('entres la valeurs de la profondeur du paralèlépipède réctangle')
c = input()
d = float(c)

print('entres la valeurs de la largeur du paralèlépipède rectangle')
e = input()
f = float(e)

i = b*d*f

print('entre la valeur du rayon de cercle')
g = input()
h = float(g)

j = 4/3*3.14*h*h*h 


if (j < i):
    print('le volume du paralèlépipèdes réctangle est plus grand que celui du cercle')
else:
    print('le volume du cercle est plus grand que celui du paralèlépipède réctangle')








