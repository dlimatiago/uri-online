cont = notas = 0
while True:
    if cont == 2:
        print('media = {:.2f}'.format(notas / 2))
        break
    nota = float(input())
    if 0 <= nota <= 10:
        cont += 1
        notas += nota
    else:
        print('nota invalida')
