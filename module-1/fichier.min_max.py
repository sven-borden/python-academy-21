def fonction(x, y, z):
    if x > y and x > z:
        a = x
    if y > x and y > z:
        a = y
    if z > x and z > y:
        a = z
   
    if z == x and z > y: 
        a = z
    if y == z and y > x:
        a = y
    if x == y and x > z:      
        a = x
    if x == y == z:
        a = x

    return a

v = fonction(12, 10, 10)



print(v)

x = min([10, 11, 12])

x = max([10, 11, 12])
 
print (x)











