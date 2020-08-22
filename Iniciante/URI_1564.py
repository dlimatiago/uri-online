# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

while True:
    try:
        reclama = int(input())
    except:
        break
    else:
        if reclama == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')
