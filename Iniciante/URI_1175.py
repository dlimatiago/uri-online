vetor = [int(input()) for _ in range(20)]
vetor = vetor[::-1]
for i, v in enumerate(vetor):
    print('N[{}] = {}'.format(i, v))
