O = str(input()).strip()
matriz = []
for _ in range(12):
    linha = list(map(float, [float(input()) for _ in range(12)]))
    matriz.append(linha)
soma = ele = 0
ls, li = 7, 5
for linha in range(7, 12):
    for coluna in range(li, ls):
        soma += matriz[linha][coluna]
        ele += 1
    li -= 1
    ls += 1
if O in 'Mm':
    media = soma / ele
    print('{:.1f}'.format(media))
elif O in 'Ss':
    print('{:.1f}'.format(soma))
