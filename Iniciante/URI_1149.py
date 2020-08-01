valores = list(map(int, input().split()))
A = valores[0]
N = valores[len(valores) - 1]

soma = 0

for i in range(N):
    soma += A + i
print(soma)
