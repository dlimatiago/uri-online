def fib(n):
    vetor = [0, 1]
    if n > 1:
        for i in range(2, n + 1):
            fb = vetor[i - 1] + vetor[i - 2]
            vetor.append(fb)
    return vetor[n]


t = int(input())
for _ in range(t):
    x = int(input())
    f = fib(x)
    print('Fib({}) = {}'.format(x, f))
