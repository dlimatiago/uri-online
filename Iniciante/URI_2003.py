# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

while True:
    try:
        h, m = map(int, input().split(':'))
    except:
        break
    else:
        atraso = h * 60 + m - 420
        if atraso < 0:
            atraso = 0
        print(f'Atraso maximo: {atraso}')
