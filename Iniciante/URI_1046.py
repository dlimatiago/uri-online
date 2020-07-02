ini, fim = input().split()
ini, fim = int(ini), int(fim)

time = fim - ini
if time < 0:
    time = 24 + time
elif time == 0:
    time = 24
else:
    time = time
print('O JOGO DUROU {} HORA(S)'.format(time))
