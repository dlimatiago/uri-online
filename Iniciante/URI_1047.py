hi, mi, hf, mf = input().split()
hi, mi, hf, mf = int(hi), int(mi), int(hf), int(mf)

timei, timef = hi*60 + mi, hf*60 + mf
delta = timef - timei
if delta < 0:
  delta = 24*60 + delta
durh = delta // 60
durm = delta - durh*60

if durh == durm == 0:
  durh, durm = 24, 0

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(durh, durm ))
