while True:
    ordem = int(input())
    if ordem == 0:
        break
    for linha in range(ordem):
        print('{:>3}'.format(linha), end='')
        for coluna in range(ordem-1):
            print('{:>3}'.format(coluna), end='')
        print()
    print()
