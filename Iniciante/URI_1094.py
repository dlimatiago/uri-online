N = int(input())

c = s = r = total = 0

for vezes in range(N):
    Quantia, Tipo = str(input()).split()
    Quantia, Tipo = int(Quantia), Tipo.strip()
    if 1 <= Quantia <= 15:
        total += Quantia
        s = s + Quantia if Tipo in 'Ss' else s
        r = r + Quantia if Tipo in 'Rr' else r
        c = c + Quantia if Tipo in 'Cc' else c

print('Total: {t} cobaias\n'
      'Total de coelhos: {C}\n'
      'Total de ratos: {R}\n'
      'Total de sapos: {S}\n'
      'Percentual de coelhos: {PC:.2f} %\n'
      'Percentual de ratos: {PR:.2f} %\n'
      'Percentual de sapos: {PS:.2f} %'.format(t=total, C=c,
                                               R=r, S=s, PC=(c / total) * 100,
                                               PR=(r / total) * 100, PS=(s / total) * 100))
