# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')


def buscar(s, q):
    for _ in range(q):
        achei = 0
        sub = input()
        for letra in range(len(s)):
            if s[letra] == sub[achei]:
                achei += 1
            if achei == len(sub):
                print('Yes')
                break
        else:
            print('No')


casos = int(input())

for _ in range(casos):
    string = input()
    n = int(input())
    buscar(string, n)
