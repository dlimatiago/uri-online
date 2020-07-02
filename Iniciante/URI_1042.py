num = str(input()).split()
x, y, z = int(num[0]), int(num[1]), int(num[2])

if x < y and x < z:
    menor = x
elif y < x and y < z:
    menor = y
elif z < x and z < y:
    menor = z
if menor == x:
    print(x)
    if y < z:
        print(y)
        print(z)
    else:
        print(z)
        print(y)
if menor == y:
    print(y)
    if x < z:
        print(x)
        print(z)
    else:
        print(z)
        print(x)
if menor == z:
    print(z)
    if x < y:
        print(x)
        print(y)
    else:
        print(y)
        print(x)
print()
print(x)
print(y)
print(z)
