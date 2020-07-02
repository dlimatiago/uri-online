dentro = 0

N = int(input())
if N < 10000:
    for i in range(N):
        X = int(input())
        if -10**7 < X < 10**7:
            if X in range(10, 20):
                dentro += 1
fora = N - dentro
print('{} in\n{} out'.format(dentro, fora))
