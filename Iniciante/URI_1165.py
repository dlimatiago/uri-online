def primo(x):
    div = 0
    for n in range(1, x + 1):
        if x % n == 0:
            div += 1
        if div > 2:
            print(x, 'nao eh primo')
            return 0
    if div == 2:
        print(x, 'eh primo')


testes = int(input())
for k in range(testes):
    valor = int(input())
    primo(valor)
