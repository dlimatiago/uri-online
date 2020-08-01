n = int(input())
if n == 0:
    print(0)
else:
    for x in range(1, n + 1):
        if not n % x:
            print(x)
