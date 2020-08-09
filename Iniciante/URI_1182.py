c, op = int(input()), str(input()).strip()
matriz = []
for _ in range(12):
    linha = list(map(float, [float(input()) for _ in range(12)]))
    matriz.append(linha)
if op in 'Mm':
    from statistics import mean as m
    val = []
    for l in matriz:
        val.append(l[c])
    media = m(val)
    print('{:.1f}'.format(media))
elif op in 'Ss':
    soma = 0
    for l in matriz:
        soma += l[c]
    print('{:.1f}'.format(soma))
