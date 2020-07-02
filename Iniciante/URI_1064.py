c = m = 0
for i in range(6):
    v = float(input())
    if v > 0:
        c += 1
        m += v
print('{} valores positivos\n{:.1f}'.format(c, m/c))
