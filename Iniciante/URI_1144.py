n = int(input())

for i in range(1, n + 1):
    q, c = i ** 2, i ** 3
    print('{} {} {}'.format(i, q, c))
    print('{} {} {}'.format(i, q + 1, c + 1))
