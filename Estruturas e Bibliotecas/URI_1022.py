def conta(n1, d1, op, n2, d2):
    if op == '+':
        num = (n1 * d2) + (n2 * d1)
        den = d1 * d2
    elif op == '-':
        num = (n1 * d2) - (n2 * d1)
        den = d1 * d2
    elif op == '*':
        num = n1 * n2
        den = d1 * d2
    elif op == '/':
        num = n1 * d2
        den = n2 * d1
    return num, den


def mdc(a, b):
    ma, mb = abs(a), abs(b)
    menor = min(ma, mb)
    maior = max(ma, mb)
    divisor = menor
    while divisor > 1:
        if menor % divisor == 0:
            if maior % divisor == 0:
                return divisor
        divisor -= 1
    return 1


N = int(input())
for i in range(N):
    exp = input().strip().split(' ')
    n1, d1, op, n2, d2 = int(exp[0]), int(exp[2]), exp[3], int(exp[4]), int(exp[6])
    num, den = conta(n1, d1, op, n2, d2)
    mxdc = mdc(num, den)
    rnum, rden = num//mxdc, den//mxdc
    print('{}/{} = {}/{}'.format(num, den, rnum, rden))
