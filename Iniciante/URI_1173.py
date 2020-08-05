valor = int(input())
vetor = []
for k in range(10):
    if k == 0:
        vetor.append(valor)
    else:
        vetor.append(vetor[k-1]*2)

for i, v in enumerate(vetor):
    print('N[{}] = {}'.format(i, v))
