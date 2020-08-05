vetor = [float(input()) for _ in range(100)]
for i, v in enumerate(vetor):
    if v <= 10:
        print('A[{}] = {}'.format(i, v))
