N = int(input())
if 2 < N < 1000:
    for m in range(1, 11):
        print('{} x {} = {}'.format(m, N, N*m))
