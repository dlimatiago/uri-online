x, y = map(int, input().split())

inicio = min(x, y)
parada = max(x, y) + 1

soma = [val if val >= 13 and not val % 13 == 0 else 0 for val in range(inicio, parada)]
print(sum(soma))
