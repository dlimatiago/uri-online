trocos_p = [7, 12, 22, 52, 102, 15, 25, 55, 105, 30, 60, 110, 70, 120, 150]
while True:
    pagar, receber = map(int, input().split())
    if pagar == receber == 0:
        break
    troco = receber - pagar
    if troco not in trocos_p:
        print('impossible')
    else:
        print('possible')
