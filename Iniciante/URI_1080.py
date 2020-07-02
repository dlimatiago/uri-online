valores = list()
for i in range(100):
    valores.append(int(input()))
maior = max(valores)
pos = valores.index(maior)
print(maior)
print(pos+1)
