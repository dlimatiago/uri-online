# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

while True:
    valores = list(map(int, input().split()))
    if valores[0] == 0:
        break
    else:
        com, larg, por = valores[0], valores[1], valores[2]
    atotal = com * larg * (100 / por)
    print(int(atotal ** 0.5))
