testes = int(input())

for k in range(testes):
    valor = int(input())
    perfeitos = [6, 28, 496, 8128, 33550336, 8589869056]

    if valor in perfeitos:
        print(valor, 'eh perfeito')
    else:
        print(valor, 'nao eh perfeito')
