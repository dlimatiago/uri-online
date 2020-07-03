while True:
    x, y = map(int, input().split())
    if x == y:
        break
    maior = max(x, y)
    print('Decrescente' if x == maior else 'Crescente')
