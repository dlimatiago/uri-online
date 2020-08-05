vetor = list(map(lambda x: 1 if x <= 0 else x, [int(input()) for _ in range(10)]))
for i, v in enumerate(vetor):
    print('X[{}] = {}'.format(i, v))
