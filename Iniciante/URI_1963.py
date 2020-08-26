antigo, novo = map(float, input().split())
porc = (novo - antigo) / antigo
print(f'{porc * 100:.2f}%')
