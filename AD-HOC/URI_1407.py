# from Teste.Testador import Testes
# t = Testes('C:/Users/tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

while True:
    sorteios_passados, n_aposta, n_max = map(int, input().split())

    if sorteios_passados + n_aposta + n_max == 0:
        break

    saiu = [list(map(int, input().split())) for _ in range(sorteios_passados)]

    numero, ocorrencia = [], []
    for n in range(1, n_max + 1):
        vezes = 0
        for resultados in saiu:
            vezes += resultados.count(n)
        numero.append(n)
        ocorrencia.append(vezes)

    menor = min(ocorrencia)
    apareceu = ocorrencia.count(menor)
    pos, start = [], 0

    for _ in range(apareceu):
        achei = ocorrencia.index(menor, start)
        pos.append(achei)
        start = achei + 1

    final = ''
    for p in pos:
        final += f'{numero[p]} '
    print(final.rstrip())
