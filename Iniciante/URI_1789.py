# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')


while True:
    try:
        qLesmas = int(input())
        vGrupo = list(map(int, input().split()))
    except:
        break
    else:
        veloz = max(vGrupo)
        if veloz < 10:
            print(1)
        elif veloz < 20:
            print(2)
        else:
            print(3)
