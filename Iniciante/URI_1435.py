# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

while True:
    ordem = int(input())
    if ordem == 0:
        break
    matriz = [[1 for _ in range(ordem)] for _ in range(ordem)]

    i, f = 1, ordem - 1
    while (f - i) >= 1:
        for x in range(i, f):
            for y in range(i, f):
                matriz[x][y] += 1
        i += 1
        f -= 1

    for linha in range(ordem):
        saida = ''
        for coluna in range(ordem):
            saida += ' %3d' % matriz[linha][coluna]
        print(saida[1:])
    print('')
