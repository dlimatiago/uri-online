values = str(input()).split()
A, B, C, D = int(values[0]), int(values[1]), int(values[2]), int(values[3])

if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
