x, y = int(input()), int(input())

i = min(x, y) + 1
f = max(x, y)

valores = {val if val % 5 == 2 or val % 5 == 3 else 0for val in range(i, f)}

valores.remove(0)
valores = list(valores)
valores.sort()

for v in valores:
    print(v)
