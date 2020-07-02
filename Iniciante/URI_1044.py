a, b = input().split()
a, b = int(a), int(b)

valor = a % b if a > b else b % a

if valor == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
