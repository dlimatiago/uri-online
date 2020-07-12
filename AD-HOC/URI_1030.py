def sobrevivente(iterable, step):
    from collections import deque as dq

    d = dq(iterable)
    p = 0
    while len(d) > 1:
        d.rotate(-step)
        d.pop()
    return list(d)


vezes = int(input())
for v in range(1, vezes + 1):
    pessoas, passo = map(int, input().split())

    vivos = list(range(1, pessoas + 1))
    vivo = sobrevivente(vivos, passo)

    print('Case {}: {}'.format(v, vivo[0]))
