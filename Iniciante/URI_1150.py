x = int(input())
while True:
    z = int(input())
    if z > x:
        break

prox = x + 1
soma = x
cont = 1
while True:
    soma += prox
    cont += 1
    if soma > z:
        print(cont)
        break
    prox += 1
