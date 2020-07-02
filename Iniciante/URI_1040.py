grades = str(input()).split()
N1, N2 = round(2*float(grades[0]), 2), round(3*float(grades[1]), 2)
N3, N4 = round(4*float(grades[2]), 2), round(float(grades[3]), 2)

med = (N1 + N2 + N3 + N4) / 10
print('Media: {}'.format(round(med, 1)))

if med >= 7.0:
  print('Aluno aprovado.')
elif 6.9 >= med >= 5.0:
  print('Aluno em exame.')
  exam = round(float(input()), 1)
  print('Nota do exame: {}'.format(exam))
  new_med = round((med + exam) / 2, 1)
  if new_med >= 5.0:
    print('Aluno aprovado.')
    print('Media final: {}'.format(new_med))
  else:
      print('Aluno reprovado.')
      print('Media final: {}'.format(new_med))
else:
  print('Aluno reprovado.')
