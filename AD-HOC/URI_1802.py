# cat = [[2, 5, 6, 3, 8], [9, 6, 3, 1, 5], [4, 8, 5, 2, 6], [3, 2, 4, 9, 5], [7, 8, 5, 1, 4]]
cat = []
for i in range(6):

    dados = input().split()
    quant, valores = int(dados[0]), list(map(int, dados[1:]))

    if i < 5:
        valores.sort()
        cat.append(valores)
    if i == 5:
        dist = quant

somas = []
for p in cat[0]:
    for m in cat[1]:
        for f in cat[2]:
            for q in cat[3]:
                for b in cat[4]:
                    valor = p + m + f + q + b
                    somas.append(valor)

somas = list(somas)
somas.sort(reverse=True)
maiscaro = sum(somas[:dist])
print(maiscaro)
