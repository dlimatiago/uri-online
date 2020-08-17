def estiagem(ca, first=True):
    mensal = moradores = 0

    for _ in range(ca):
        m, cm = map(int, input().split())

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

    s = '.'
    i, d = str(mensal / moradores).split(s)
    md = i + s + d[:2]
    return float(md)


cidade = 1
casos = int(input())
while casos > 0:

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

    casos = int(input())
    if casos == 0:
        break
    print()
    cidade += 1
