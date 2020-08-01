vezes = int(input())

for k in range(vezes):
    soma = cont = 0
    inico, quant = map(int, input().split())
    if inico % 2:
        s = inico
        while cont < quant:
            soma += s
            cont += 1
            s += 2
        print(soma)
    else:
        s = inico + 1
        while cont < quant:
            soma += s
            cont += 1
            s += 2
        print(soma)
