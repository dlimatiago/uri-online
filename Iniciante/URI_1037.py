n = float(input())

if 25 >= n >= 0:
    print('Intervalo [0,25]')
elif 50 >= n > 25:
    print('Intervalo (25,50]')
elif 75 >= n > 50:
    print('Intervalo (50,75]')
elif 100 >= n > 75:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
