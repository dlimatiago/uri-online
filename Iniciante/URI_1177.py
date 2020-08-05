t = int(input())
vetor = []
while len(vetor) < 1000:
    for i in range(t):
        if len(vetor) == 1000:
            break
        vetor.append(i)
for i, v in enumerate(vetor):
    print('N[{}] = {}'.format(i, v))
