def busca(peças, chute, n):
    b = n // 2
    p = 0
    while True:
        if chute >= peças[b]:
            peças = peças[b:]
            p += b
        elif chute < peças[b]:
            peças = peças[:b]
        b //= 2

        if len(peças) <= 10 or chute == peças[b]:
            if chute in peças:
                p += peças.index(chute) + 1
                return p
            else:
                return -1


case = 1
while True:
    quant, tent = map(int, input().split())
    if quant == 0 and tent == 0 or case > 65 or quant > 10000 or quant < 0 or tent < 0:
        break

    marbles = []
    for m in range(quant):
        marbles.append(int(input()))
    marbles.sort()
    chutes = []
    for c in range(tent):
        chutes.append(int(input()))

    print('CASE# {}:'.format(case))
    for ch in chutes:
        r = busca(marbles, ch, quant)
        print('{} {}'.format(ch, 'found at {}'.format(r) if r != -1 else 'not found'))
    case += 1

