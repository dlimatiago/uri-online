O = str(input()).strip()
matriz = []
for _ in range(12):
    linha = list(map(float, [float(input()) for _ in range(12)]))
    matriz.append(linha)
soma = ele = li = 0
ls = 11
for linha in range(12):
    for coluna in range(12):
        if li < coluna < ls:
            soma += matriz[linha][coluna]
            ele += 1
    li += 1
    ls -= 1
if O in 'Mm':
    media = soma / ele
    print('{:.1f}'.format(media))
elif O in 'Ss':
    print('{:.1f}'.format(soma))
