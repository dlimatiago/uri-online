while True:
    cont = r = notas = 0
    while cont < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            cont += 1
            notas += nota
        else:
            print('nota invalida')
    print('media = {:.2f}'.format(notas / 2))
    while r not in (1, 2):
        print('novo calculo (1-sim 2-nao)')
        r = int(input())
    if r == 2:
        break
