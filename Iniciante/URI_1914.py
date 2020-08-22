ct = int(input())
par, impar = 'PAR', 'IMPAR'
for _ in range(ct):
    opc = list(map(str, input().split()))
    n1, n2 = map(int, input().split())
    soma = n1 + n2
    if not soma % 2:
        if par == opc[1]:
            print(opc[0])
        else:
            print(opc[2])
    else:
        if impar == opc[1]:
            print(opc[0])
        else:
            print(opc[2])
