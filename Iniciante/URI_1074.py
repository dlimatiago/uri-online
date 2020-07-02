N = int(input())
if N < 10000:
    for i in range(N):
        X = int(input())
        if -10**7 < X < 10**7:
            if X % 2 == 0 and X < 0:
                print('EVEN NEGATIVE')
            elif X % 2 == 0 and X > 0:
                print('EVEN POSITIVE')
            elif X % 2 == 1 and X < 0:
                print('ODD NEGATIVE')
            elif X % 2 == 1 and X > 0:
                print('ODD POSITIVE')
            elif X == 0:
                print('NULL')
