# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')


abas, n = map(int, input().split())

abertas = abas
for _ in range(n):
    action = input().lower()

    if action in 'clicou':
        abertas -= 1
    elif action in 'fechou':
        abertas += 1
print(abertas)
