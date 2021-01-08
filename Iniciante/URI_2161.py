def raiz(x):
    if x == 0:
        return 6
    x = 6 + 1/raiz(x - 1)
    return x


print(f'{raiz(int(input())) - 3:.10f}')
