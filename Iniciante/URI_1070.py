X = int(input())
c, X = 0, X + 1 if X % 2 == 0 else X

if X > 0:
    while c < 6:
        print(X)
        X += 2
        c += 1
