from itertools import permutations as per
# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

varetas = list(map(int, input().split()))
possibilidades = list(per(varetas, 3))
v = True
for dim in possibilidades:
    m1, m2, m3 = map(int, dim)
    if abs(m2 - m3) < m1 < m2 + m3 and abs(m1 - m3) < m2 < m1 + m3 and abs(m1 - m2) < m3 < m1 + m2:
        print('S')
        v = False
        break
if v:
    print('N')
