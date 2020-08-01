soma = 1
n, d = 3, 2
while n <= 39:
    soma += n / d
    n += 2
    d *= 2
print('{:.2f}'.format(soma))
