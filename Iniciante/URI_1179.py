par, imp = [], []
cont = p = i = 0
while cont < 15:
    x = int(input())
    if not x % 2:
        par.append(x)
        p = p + 1
    else:
        imp.append(x)
        i = i + 1
    if p > 4:
        for c in range(0, 5):
            print('par[{}] = {}'.format(c, par[c]))
        par.clear()
        p = 0
    if i > 4:
        for c in range(0, 5):
            print('impar[{}] = {}'.format(c, imp[c]))
        imp.clear()
        i = 0
    cont = cont + 1
if i > 0:
    for j in range(i):
        print('impar[{}] = {}'.format(j, imp[j]))
if p > 0:
    for h in range(p):
        print('par[{}] = {}'.format(h, par[h]))
