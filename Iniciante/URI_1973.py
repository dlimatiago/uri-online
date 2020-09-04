# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

stars = int(input())
lambs = [int(i) for i in input().split()]
tlambs = sum(lambs)
taken = [0] * stars
nxt = 0

while 0 <= nxt < stars:
    direction = lambs[nxt] % 2
    if lambs[nxt] > 0:
        lambs[nxt] -= 1
        taken[nxt] = 1
        tlambs -= 1
    if direction:
        nxt += 1
    else:
        nxt -= 1


taken = taken.count(1)
print(taken, tlambs)
