# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

while True:
    try:
        v, d = float(input()), float(input())
        pi = 3.14
        h = (4 * v) / (pi * d ** 2)
        ab = pi * (d / 2) ** 2
        print(f'ALTURA = {h:.2f}')
        print(f'AREA = {ab:.2f}')
    except:
        break
