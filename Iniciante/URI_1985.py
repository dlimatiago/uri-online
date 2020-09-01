# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

prod = {1001: 1.5,
        1002: 2.5,
        1003: 3.5,
        1004: 4.5,
        1005: 5.5}

qtd = int(input())
total = 0
for _ in range(qtd):
    cod, tot = map(int, input().split())
    total += prod[cod] * tot
print(f'{total:.2f}')
