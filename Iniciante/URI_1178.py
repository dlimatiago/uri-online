valor = float(input())
vetor = []
for k in range(100):
    if k == 0:
        vetor.append(valor)
    else:
        n = vetor[k-1] / 2
        vetor.append(n)

for i, v in enumerate(vetor):
    print('N[{}] = {:.4f}'.format(i, v))
