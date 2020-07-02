ps = n = i = p = 0
for k in range(5):
    v = int(input())
    if v % 2 == 0:
        p += 1
    if v > 0:
        ps += 1
    if v < 0:
        n += 1
    if v % 2 == 1:
        i += 1

print('{} valor(es) par(es)\n{} valor(es) impar(es)\n'
      '{} valor(es) positivo(s)\n{} valor(es) negativo(s)'.format(p, i, ps, n))
