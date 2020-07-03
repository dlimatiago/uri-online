vezes = int(input())
for testes in range(vezes):
    num, den = map(int, input().split())
    if den == 0:
        print('divisao impossivel')
        continue
    else:
        res = num / den
        print('{:.1f}'.format(res))
