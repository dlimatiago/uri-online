values = str(input()).split()
A, B, C = float(values[0]), float(values[1]), float(values[2])
areat = 0.5 * (A * C)
areac = 3.14159 * (C**2)
areatpz = ((A + B) * C) / 2
areasq = B**2
arearec = A * B
print('TRIANGULO: {:.3f}\n'
      'CIRCULO: {:.3f}\n'
      'TRAPEZIO: {:.3f}\n'
      'QUADRADO: {:.3f}\n'
      'RETANGULO: {:.3f}'.format(areat, areac, areatpz, areasq, arearec))
