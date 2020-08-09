op = str(input()).strip()
matriz = []
for _ in range(12):
    linha = list(map(float, [float(input()) for _ in range(12)]))
    matriz.append(linha)
soma = ele = 0
for linha in range(12):
    for coluna in range(12):
        if coluna < linha:
            soma += matriz[linha][coluna]
            ele += 1
if op in 'Mm':
    media = soma / ele
    print('{:.1f}'.format(media))
elif op in 'Ss':
    print('{:.1f}'.format(soma))
