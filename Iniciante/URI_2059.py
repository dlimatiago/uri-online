p, j1, j2, r, a = map(int, input().split())
v = 0

if not j1 + j2 % 2:
    if p == 1:
        v = 1
    else:
        v = 2
else:
    if p == 0:
        v = 1
    else:
        v = 2

if r == 1 and a == 1:
    print('Jogador 2 ganha!')
elif r == 1 and a == 0:
    print('Jogador 1 ganha!')
elif r == 0 and a == 1:
    print('Jogador 1 ganha!')
elif r == 0 and a == 0:
    if v == 1:
        print('Jogador 1 ganha!')
    elif v == 2:
        print('Jogador 2 ganha!')
