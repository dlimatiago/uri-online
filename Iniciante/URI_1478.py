# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

while True:
    ordem = int(input())
    if ordem == 0:
        break
    matriz = []
    i, f = 1, ordem
    for x in range(ordem):
        aux = []
        if x == 0:
            aux = list(range(1, ordem + 1))
        elif x + 1 == ordem:
            aux = list(range(ordem, 0, -1))
        else:
            for p in range(i, 0, -1):
                aux.append(p)
            for m in range(2, f + 1):
                aux.append(m)
        i += 1
        f -= 1
        matriz.append(aux)

    for linha in range(ordem):
        saida = ''
        for coluna in range(ordem):
            saida += ' %3d' % matriz[linha][coluna]
        print(saida[1:])
    print('')
