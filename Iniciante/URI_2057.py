# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

saida, tempo, fuso = map(int, input().split())
horario = saida + tempo + fuso
if horario >= 24:
    horario -= 24
elif horario < 0:
    horario = 24 + horario
print(horario)

