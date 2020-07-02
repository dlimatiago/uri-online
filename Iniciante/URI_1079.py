N = int(input())
for vezes in range(N):
    a, b, c = input().split()
    a, b, c = 2*float(a), 3*float(b), 5*float(c)
    m = (a + b + c) / 10
    print('{:.1f}'.format(m))
