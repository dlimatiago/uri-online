case = 1

while True:
    try:
        sub, seq = input(), input()
        print(f'Caso #{case}:')

        vezes = seq.count(sub)
        if not vezes:
            print('Nao existe subsequencia')
        else:
            print(f'Qtd.Subsequencias: {vezes}')
            pos = seq.rfind(sub)
            print(f'Pos: {pos + 1}')
        print()

        case += 1
    except EOFError:
        break
