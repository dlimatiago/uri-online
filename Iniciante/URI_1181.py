l, op = int(input()), str(input()).strip()
matriz = []
for _ in range(12):
    linha = list(map(float, [float(input()) for _ in range(12)]))
    matriz.append(linha)
if op in 'Mm':
    media = sum(matriz[l]) / 12
    print('{:.1f}'.format(media))
elif op in 'Ss':
    soma = sum(matriz[l])
    print('{:.1f}'.format(soma))
