# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

pulo, canos = map(int, input().split())
altura = list(map(int, input().split()))

res = 0
for x in range(canos - 1):
    res += 0 if abs(altura[x] - altura[x + 1]) <= pulo else 1
    if res != 0:
        print('GAME OVER')
        break
if not res:
    print('YOU WIN')
