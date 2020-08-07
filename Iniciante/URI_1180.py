n = int(input())
lista = list(map(int, input().split()))
menor = min(lista)
pos = lista.index(menor)
print('Menor valor: {}\n'
      'Posicao: {}'.format(menor, pos))
