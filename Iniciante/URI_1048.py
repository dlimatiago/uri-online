wage = float(input())

if 400.00 >= wage >= 0:
  reaj = wage*.15
  por = 15
  new = wage + reaj
elif 800.00 >= wage >= 400.01:
  reaj = wage*.12
  por = 12
  new = wage + reaj
elif 1200.00>= wage >= 800.01:
  reaj = wage*.1
  por = 10
  new = wage + reaj
elif 2000.00 >= wage >= 1200.01:
  reaj = wage*.07
  por = 7
  new = wage + reaj
elif wage > 2000.00:
  reaj = wage*.04
  por = 4
  new = wage + reaj

print('Novo salario: {:.2f}\n'
      'Reajuste ganho: {:.2f}\n'
      'Em percentual: {} %'.format(new, reaj, por))
