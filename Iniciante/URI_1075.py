N = int(input())
if N < 10000:
    for d in range(1, 10000):
        if d % N == 2:
            print(d)
