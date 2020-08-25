paginas = int(input())
u, d, c, m = paginas // 1 % 10, paginas // 10 % 10, paginas // 100 % 10, paginas // 1000 % 10

romano = ''
if m != 0:
    romano += 'M' * m
if 1 <= c < 4:
    romano += 'C' * c
elif 5 < c < 9:
    c -= 5
    romano += 'D' + ('C' * c)
elif c == 4:
    romano += 'CD'
elif c == 9:
    romano += 'CM'
elif c != 0:
    romano += 'D'
if 1 <= d < 4:
    romano += 'X' * d
elif 5 < d < 9:
    d -= 5
    romano += 'L' + ('X' * d)
elif d == 4:
    romano += 'XL'
elif d == 9:
    romano += 'XC'
elif d != 0:
    romano += 'L'
if 1 <= u < 4:
    romano += 'I' * u
elif 5 < u < 9:
    u -= 5
    romano += 'V' + ('I' * u)
elif u == 4:
    romano += 'IV'
elif u == 9:
    romano += 'IX'
elif u != 0:
    romano += 'V'

print(romano)

