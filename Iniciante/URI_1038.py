info = str(input()).split()
cod, quant = int(info[0]), int(info[1])

if cod == 1:
    bill2pay = 4 * quant
elif cod == 2:
    bill2pay = 4.5 * quant
elif cod == 3:
    bill2pay = 5 * quant
elif cod == 4:
    bill2pay = 2 * quant
elif cod == 5:
    bill2pay = 1.5 * quant

print('Total: R$ {:.2f}'.format(bill2pay))
