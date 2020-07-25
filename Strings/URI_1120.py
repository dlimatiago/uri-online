while True:
    tecla, valor = input().strip().split()
    if tecla in '0' and valor in '0':
        break

    if tecla in valor:
        valor = valor.split(tecla)
        novo = ''.join(valor)
        if novo in '':
            novo = '0'
        print(int(novo))
    else:
        print(int(valor))
