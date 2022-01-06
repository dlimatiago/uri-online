linhas, colunas = map(int, input().split())

radar = []  # matriz com as frequencias
sabre = []  # coordenadas do sabre
x = y = 0

for m in range(linhas):
    linha = input().replace(' ', '')
    triple7 = True if linha.count('777') == 1 else False

#     linha = list(map(int, input().split()))
#     try:
#         rep = linha.count(42)
#         inicio = 0
#         for r in range(rep):
#             c = linha.index(42, inicio)
#             if c + 1 < colunas and m + 1 < linhas and c - 1 >= 0 and m - 1 >= 0:
#                 sabre.append((m, c))
#             inicio = c + 1
#
#     except ValueError:
#         pass
#     radar.append(linha)
#
#
# for ponto in sabre:
#     i, j = ponto[0], ponto[1]
#
#     redor = [radar[i-1][j] == 7 and radar[i+1][j] == 7,
#              radar[i][j-1] == 7 and radar[i][j+1] == 7,
#              radar[i-1][j-1] == 7 and radar[i+1][j+1] == 7,
#              radar[i-1][j+1] == 7 and radar[i+1][j-1] == 7
#              ]
#     if all(redor):
#         x, y = i+1, j+1
#         break

print(x, y)
