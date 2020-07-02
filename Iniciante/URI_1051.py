wage = float(input())

if wage <= 2000.00:
    print('Isento')

elif wage <= 3000.00:
    tax = (wage - 2000.00) * .08
    print('R$ {:.2f}'.format(tax))

elif wage <= 4500.00:
    tax = 1000.00 * .08 + (wage - 3000.00) * .18
    print('R$ {:.2f}'.format(tax))

elif 4500.00 < wage:
    tax = 1000.00 * .08 + 1500.00 * .18 + (wage - 4500.00) * .28
    print('R$ {:.2f}'.format(tax))
