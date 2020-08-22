n = int(input())
pessoas = list(map(int, input().split()))
menor = min(pessoas)
print(pessoas.index(menor) + 1)
