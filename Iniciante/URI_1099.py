vezes = int(input())
tudo = []
for teste in range(vezes):

    a, b = map(int, input().split())
    maior, menor = max(a, b), min(a, b)
    somaimpar = sum([x if x % 2 == 1 and x != menor else 0 for x in range(menor, maior)])
    tudo.append(somaimpar)
for i in tudo:
    print(i)
