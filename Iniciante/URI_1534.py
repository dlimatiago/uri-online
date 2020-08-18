# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

while True:
    try:
        ordem = int(input())
    except:
        break
    else:
        matriz = []
        for x in range(ordem):
            aux = []
            for y in range(ordem):
                if x == 0 and y == 0 or x + 1 == ordem and y + 1 == ordem:
                    aux.append(1)
                elif x == 0 and y + 1 == ordem or x + 1 == ordem and y == 0:
                    aux.append(2)
                else:
                    aux.append(3)
            matriz.append(aux)

        um, dois = 1, ordem - 2
        for i, l in enumerate(matriz):
            if i == 0 or i + 1 == ordem:
                continue
            else:
                if um == dois:
                    l[um] = 2
                else:
                    l[um] = 1
                    l[dois] = 2
                um += 1
                dois -= 1

        for x in range(ordem):
            for y in range(ordem):
                print(matriz[x][y], end='')
            print()
