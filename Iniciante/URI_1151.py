n = int(input())

if n == 1:
    print(0)
else:
    n1, n2, cont = 0, 1, 3
    print('{} {} '.format(n1, n2), end='')
    while cont <= n:
        fib = n1 + n2
        print(fib, end=(' ' if cont < n else ''))
        n1 = n2
        n2 = fib
        cont += 1
    print()
