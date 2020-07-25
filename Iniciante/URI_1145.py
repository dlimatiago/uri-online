passo, limite = map(int, input().strip().split())
c = 1
while c <= limite:
    if c % passo == 0:
        print(c)
    else:
        print(c, end=' ')
    c += 1
