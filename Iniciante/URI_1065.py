c = 0
for i in range(5):
    v = int(input())
    if v % 2 == 0:
        c += 1
print('{} valores pares'.format(c))
