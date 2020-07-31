def correcao(x):
    inteiro, decimal = x.split('.')
    decimal = decimal[:2]
    valor = inteiro + '.' + decimal
    return float(valor)


def estiagem(ca, first=True):
    mensal = moradores = 0

    for o in range(ca):
        m, cm = map(int, input().split())
        if 1 <= m <= 10 and 1 <= cm <= 200:

            faixa = cm // m
            mensal += cm
            moradores += m

            if first:
                faixas[faixa] = m
                first = False
            elif faixa not in faixas:
                faixas[faixa] = m
            else:
                faixas[faixa] += m

    md = correcao(str(mensal / moradores))
    return md


cidade = 1
while True:
    casos = int(input())
    if casos == 0:
        break

    global faixas
    faixas = dict()
    media = estiagem(casos)

    faixas = {key: faixas[key] for key in sorted(faixas)}
    print('Cidade# {}:'.format(cidade))
    trava = 1
    for c, p in faixas.items():
        print('{}-{}'.format(p, c), end=(' ' if trava < len(faixas) else ''))
        trava += 1
    print()
    print('Consumo medio: {:.2f} m3.'.format(media))
    print()
    cidade += 1
