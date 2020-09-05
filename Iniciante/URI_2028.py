# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

caso = 1 
while True:
    try:
        ns = [0]
        n = int(input())
        if n == 0:
            print(f'Caso {caso}: {len(ns)} numero')
            print(0)
            print()
        else:
            for x in range(1, n + 1):
                for _ in range(x):
                    ns.append(x)
            print(f'Caso {caso}: {len(ns)} numeros')
            vezes = 0
            for y in ns:
                print(y, end=(' ' if vezes < len(ns) - 1 else ''))
                vezes += 1
            print()
            print()

        caso += 1
    except:
        break
