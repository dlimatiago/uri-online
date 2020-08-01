while True:
    soma = cont = 0
    inico = int(input())
    if inico == 0:
        break
    if inico % 2:
        s = inico + 1
        while cont < 5:
            soma += s
            cont += 1
            s += 2
        print(soma)
    else:
        s = inico
        while cont < 5:
            soma += s
            cont += 1
            s += 2
        print(soma)
