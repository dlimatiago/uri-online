# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

cont = soma = 0
while cont < 3:
    blink = input()

    if blink == 'caw caw':
        cont += 1
        print(soma)
        soma = 0
    else:
        soma += int(''.join('1' if i == '*' else '0' for i in blink), 2)
