while True:
    x = int(input())
    if x == 0:
        break
    for valor in range(1, x + 1):
        print(valor, end=(' ' if valor < x else ''))
    print()
