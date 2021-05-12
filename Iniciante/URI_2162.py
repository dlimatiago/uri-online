n = int(input())
h = list(map(int, input().split()))

padrao = [1 if n == 2 and h[0] == h[1] else 0]
for i in range(1, n - 1):
    padrao.append(0 if (h[i+1] > h[i] < h[i-1]) or (h[i+1] < h[i] > h[i-1]) else 1)

print(1 if sum(padrao) == 0 else 0)
