O = str(input()).strip()
matriz = []
for _ in range(12):
    linha = list(map(float, [float(input()) for _ in range(12)]))
    matriz.append(linha)
soma = ele = 0
c = 12
for linha in range(12):
    c -= 1
    for coluna in range(c):
        soma += matriz[linha][coluna]
        ele += 1
if O in 'Mm':
    media = soma / ele
    print('{:.1f}'.format(media))
elif O in 'Ss':
    print('{:.1f}'.format(soma))
