def busca(peças, chute):
    from bisect import bisect_left as bl
    pos = bl(peças, chute)

    if pos < len(peças) and peças[pos] == chute:
        return pos + 1
    else:
        return -1


case = 1
while True:
    quant, tent = map(int, input().split())
    if quant == 0 and tent == 0:
        break

    marbles = [int(input()) for m in range(quant)]
    marbles.sort()
    print('CASE# {}:'.format(case))
    for ch in range(tent):
        t = int(input())
        r = busca(marbles, t)
        print('{} {}'.format(t, 'found at {}'.format(r) if r != -1 else 'not found'))
    case += 1
