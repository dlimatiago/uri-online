N = int(input())
N1 = N
c100 = N // 100
N -= 100 * c100
c50 = N // 50
N -= 50 * c50
c20 = N // 20
N -= 20 * c20
c10 = N // 10
N -= 10 * c10
c5 = N // 5
N -= 5 * c5
c2 = N // 2
N -= 2 * c2
c1 = N // 1

print('{}'.format(N1))
print('{} nota(s) de R$ 100,00'.format(c100))
print('{} nota(s) de R$ 50,00'.format(c50))
print('{} nota(s) de R$ 20,00'.format(c20))
print('{} nota(s) de R$ 10,00'.format(c10))
print('{} nota(s) de R$ 5,00'.format(c5))
print('{} nota(s) de R$ 2,00'.format(c2))
print('{} nota(s) de R$ 1,00'.format(c1))
