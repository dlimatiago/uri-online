N = int(input())
if 5 < N < 2000:
    for q in range(1, N+1):
        if q % 2 == 0:
            print('{}^2 = {}'.format(q, q**2))
