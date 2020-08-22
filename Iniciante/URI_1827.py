# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

while True:
    try:
        ordem = int(input())
    except:
        break
    else:
        matriz = []
        dp, ds = 0, ordem - 1
        li = ordem // 3
        ls = ordem - li - 1
        for l in range(ordem):
            aux = []
            for c in range(ordem):
                if c == ordem // 2 and c == l:
                    aux.append(4)
                elif li <= c <= ls and li <= l <= ls:
                    aux.append(1)
                elif c == dp:
                    aux.append(2)
                elif c == ds:
                    aux.append(3)
                else:
                    aux.append(0)
            dp += 1
            ds -= 1
            matriz.append(aux)

        for x in range(ordem):
            for y in range(ordem):
                print(matriz[x][y], end='')
            print()
        print()
