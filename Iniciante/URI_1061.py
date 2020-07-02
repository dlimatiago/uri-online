idia = input().split()
idia = int(idia[1])
ih = str(input())
fdia = input().split()
fdia = int(fdia[1])
fh = str(input())

ihora, imin, iseg = ih.split(':')
ihora, imin, iseg = int(ihora), int(imin), int(iseg)
fhora, fmin, fseg = fh.split(':')
fhora, fmin, fseg = int(fhora), int(fmin), int(fseg)

dif_d, dif_h, dif_m, dif_s = fdia - idia, fhora - ihora, fmin - imin, fseg - iseg

if dif_h < 0:
    dif_d -= 1
    dif_h += 24
if dif_m < 0:
    dif_h -= 1
    dif_m += 60
if dif_s < 0:
    dif_m -= 1
    dif_s += 60
print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dif_d, dif_h, dif_m, dif_s))
