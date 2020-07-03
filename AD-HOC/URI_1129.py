while True:
    nquest = int(input())
    if nquest == 0:
        break

    for teste in range(nquest):
        a, b, c, d, e = map(int, input().split())
        respostas = (a, b, c, d, e)
        alternativas = ('A', 'B', 'C', 'D', 'E')
        branco = preto = 0

        for i, opc in enumerate(respostas):
            if 0 <= opc <= 127:
                preto += 1
                pos = i
            elif 127 < opc <= 255:
                branco += 1
        if branco > 4 or preto > 1:
            print('*')
        else:
            print(str(alternativas[pos]))
