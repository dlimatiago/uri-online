X, Y = int(input()), int(input())
s = 0
for i in range(X+1 if X < Y else Y+1, Y if Y > X else X):
    if i % 2 == 1:
        s += i
print(s)
