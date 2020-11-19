# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

casos = int(input())

for _ in range(casos):
    codigo = input()
    if codigo[1].islower() and codigo[0] != codigo[2]:
        resultado = int(codigo[0]) + int(codigo[2])

    elif codigo[1].isupper() and codigo[0] != codigo[2]:
        resultado = int(codigo[2]) - int(codigo[0])

    elif int(codigo[0]) == int(codigo[2]):
        resultado = soma = int(codigo[0]) * int(codigo[2])

    print(resultado)
