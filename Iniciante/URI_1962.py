# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

casos = int(input())
for _ in range(casos):
    ano = int(input())
    data = 2015 - ano
    if data < 0:
        print(abs(data) + 1, 'A.C.')
    elif data == 0:
        print('1 A.C.')
    else:
        print(data, 'D.C.')
