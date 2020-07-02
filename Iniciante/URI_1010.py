tool1 = str(input()).split()
tool2 = str(input()).split()

sub1 = int(tool1[1]) * float(tool1[2])
sub2 = int(tool2[1]) * float(tool2[2])
total = sub1 + sub2
print('VALOR A PAGAR: R$ {:.2f}'.format(total))
