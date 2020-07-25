a = g = d = 0
while True:
    while True:
        tipo = int(input())
        if tipo in (1, 2, 3, 4):
            break
    if tipo == 4:
        break

    if tipo == 1:
        a += 1
    elif tipo == 2:
        g += 1
    else:
        d += 1
print('MUITO OBRIGADO')
print('Alcool: {}\n'
      'Gasolina: {}\n'
      'Diesel: {}'.format(a, g, d))
