i = 0
inc = 0
while i <= 2:
    for j in range(1, 4):
        i = int(i) if i - int(i) == 0 else round(i, 1)
        s = int(i+j) if (i+j) - int(i+j) == 0 else round(j+i, 1)
        print('I={} J={}'.format(i, s))

    i += 0.2
