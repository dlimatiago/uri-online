while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break

    maior, menor = max(m, n), min(m, n)
    soma = 0

    for valor in range(menor, maior+1):
        print(valor, end=' ')
        soma += valor
    print('Sum={}'.format(soma))
