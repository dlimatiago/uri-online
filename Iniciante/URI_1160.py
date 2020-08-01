t = int(input())
for x in range(t):
    PA, PB, CA, CB = map(float, input().split())
    PA, PB = int(PA), int(PB)
    anos = 0
    while True:
        PA += int(PA * CA / 100)
        PB += int(PB * CB / 100)
        anos += 1

        if anos > 100 or PA > PB:
            break

    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print(anos, 'anos.')
