# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

casos = int(input())
for _ in range(casos):
    p1, p2 = input().strip().lower(), input().strip().lower()
    if p1 == 'pedra' and p2 == 'pedra':
        print('Sem ganhador')
    elif p1 == 'ataque' and p2 == 'ataque':
        print('Aniquilacao mutua')
    elif p1 == 'papel' and p2 == 'papel':
        print('Ambos venceram')
    else:
        if p1 == 'ataque' and p2 in ('pedra', 'papel'):
            print('Jogador 1 venceu')
        elif p1 in ('ataque', 'pedra') and p2 == 'papel':
            print('Jogador 1 venceu')
        elif p2 == 'ataque' and p1 in ('pedra', 'papel'):
            print('Jogador 2 venceu')
        elif p2 in ('ataque', 'pedra') and p1 == 'papel':
            print('Jogador 2 venceu')
