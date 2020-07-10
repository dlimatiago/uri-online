def ordem(p, f, n):
    t = len(f)
    juntos = [(p[item], f[item]) for item in range(t)]

    juntos.sort(key=lambda x: x[1])

    print('Cidade# {}:'.format(n))
    for i in juntos:
        print('{}-{}'.format(i[0], i[1]), end=' ')
    print()


n = 1
while True:
    casos = int(input())
    if casos == 0 or 0 > casos or casos > 1000000:
        break

    con_total = total_m = 0
    faixa, pessoa = list(), list()

    for v in range(casos):
        q_moradores, con_mensal = map(int, input().split())

        if 1 <= q_moradores <= 10 and 1 <= con_mensal <= 200:

            con_total += con_mensal
            total_m += q_moradores
            m3 = con_mensal // q_moradores

            if m3 not in faixa:
                faixa.append(m3)
                pessoa.append(q_moradores)
            else:
                pos = faixa.index(m3)
                pessoa.insert(pos, pessoa[pos] + q_moradores)
                pessoa.pop(pos+1)

    ordem(pessoa, faixa, n)
    med = con_total / total_m

    print('Consumo medio: {:.2f} m3.'.format(med))
    n += 1
