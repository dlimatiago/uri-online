def mdc(a, b):
    while b:
        a, b = b, a % b
    return a


casos = int(input())

for vez in range(casos):
    x, y = map(int, input().split())
    print(mdc(x, y))
