age = int(input())

year = age // 365
month = age - (year * 365)
month = month // 30
day = age - (year * 365) - (month * 30)
print("{} ano(s)\n"
      "{} mes(es)\n"
      "{} dia(s)".format(year, month, day))
