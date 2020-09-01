# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

alunos = int(input())
notas = []
for _ in range(alunos):
    mat, nota = map(float, input().split())
    notas += [(int(mat), nota)]

maior = max(notas, key=lambda x: x[1])
if maior[1] >= 8.0:
    print(maior[0])
else:
    print('Minimum note not reached')

