points = str(input()).split()
x, y = round(float(points[0]), 1), round(float(points[1]), 1)

if x == y == 0:
  print('Origem')
elif x == 0:
  print('Eixo Y')
elif y == 0:
  print('Eixo X')
elif x > 0 and y > 0:
  print('Q1')
elif x < 0 and y > 0:
  print('Q2')
elif x < 0 and y < 0:
  print('Q3')
elif x > 0 and y < 0:
  print('Q4')
