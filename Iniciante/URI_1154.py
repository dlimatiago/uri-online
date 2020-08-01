def media(iterable):
    return sum(iterable) / len(iterable)


ids = list()
while True:
    idade = int(input())
    if idade < 0:
        print('{:.2f}'.format(media(ids)))
        break
    ids.append(idade)
