values = str(input()).split()
A, B, C = float(values[0]), float(values[1]), float(values[2])
A, B, C =  round(A, 2), round(B, 2), round(C, 2)

delta = B**2 - (4*A*C)
if delta < 0 or A == 0:
  print('Impossivel calcular')
else:
  delta = (delta)**0.50
  R1 = (-B + delta) / (2*A)
  R2 = (-B - delta) / (2*A)
  print('R1 = {:.5f}\n'
        'R2 = {:.5f}'.format(R1, R2))
