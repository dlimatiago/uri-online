# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

while True:
    ordem = int(input())
    if ordem == 0:
        break
    matriz = []
    i, f = 0, ordem
    for _ in range(ordem):
        matriz.append(list(map(lambda x: 2 ** x, list(range(i, f)))))
        i += 1
        f += 1

    T = len(str(matriz[ordem - 1][ordem - 1]))
    for i in range(ordem):
        for j in range(ordem):
            matriz[i][j] = str(matriz[i][j])
            while len(matriz[i][j]) < T:
                matriz[i][j] = ' ' + matriz[i][j]
        M = ' '.join(matriz[i])

        print(M)
    print()
