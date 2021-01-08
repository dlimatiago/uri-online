for _ in range(int(input())):
    h, m, o = input().split()
    print(f'{h:0>2}:{m:0>2} -', 'A porta abriu!' if int(o) else 'A porta fechou!')
