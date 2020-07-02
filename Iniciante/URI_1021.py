N = round(float(input()), 2)

c100 = int(N / 100)
N -= c100*100
N = round(N, 2)

c50 = int(N / 50)
N -= c50*50
N = round(N, 2)

c20 = int(N / 20)
N -= c20*20
N = round(N, 2)

c10 = int(N / 10)
N -= c10*10
N = round(N, 2)

c5 = int(N / 5)
N -= c5*5
N = round(N, 2)

c2 = int(N / 2)
N -= c2*2
N = round(N, 2)

c1 = int(N / 1)
N -= c1
N = round(N, 2)

c050 = int(N / 0.50)
N -= c050*0.50
N = round(N, 2)

c025 = int( N / 0.25)
N -= c025*0.25
N = round(N, 2)

c010 = int(N / 0.1)
N -= c010*0.1
N = round(N, 2)

c05 = int(N / 0.05)
N -= c05*0.05
N = round(N, 2)

c01 = int(N / 0.01)
N -= c01

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(c100))
print('{} nota(s) de R$ 50.00'.format(c50))
print('{} nota(s) de R$ 20.00'.format(c20))
print('{} nota(s) de R$ 10.00'.format(c10))
print('{} nota(s) de R$ 5.00'.format(c5))
print('{} nota(s) de R$ 2.00'.format(c2))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(c1))
print('{} moeda(s) de R$ 0.50'.format(c050))
print('{} moeda(s) de R$ 0.25'.format(c025))
print('{} moeda(s) de R$ 0.10'.format(c010))
print('{} moeda(s) de R$ 0.05'.format(c05))
print('{} moeda(s) de R$ 0.01'.format(c01))
