while True:
    x = int(input())
    if x == 0:
        break

    for _ in range(x):
        v = int(input())
        if not v % 2:
            print(v * 2 - 2)
        else:
            print(v * 2 - 1)
