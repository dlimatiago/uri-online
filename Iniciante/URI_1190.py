O = str(input()).strip()
matriz = []
for _ in range(12):
    linha = list(map(float, [float(input()) for _ in range(12)]))
    matriz.append(linha)
soma = ele = 0
limite = 11
for linha in range(1, 11):
    for coluna in range(limite, 12):
        soma += matriz[linha][coluna]
        ele += 1
    if linha < 5:
        limite -= 1
    elif linha > 5:
        limite += 1

if O in 'Mm':
    media = soma / ele
    print('{:.1f}'.format(media))
elif O in 'Ss':
    print('{:.1f}'.format(soma))
