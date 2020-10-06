quant = int(input())
analise = list(map(int, input().split()))

m2, m3 = list(filter(lambda x: x % 2 == 0, analise)), list(filter(lambda x: x % 3 == 0, analise))
m4, m5 = list(filter(lambda x: x % 4 == 0, analise)), list(filter(lambda x: x % 5 == 0, analise))

print(f'{len(m2)} Multiplo(s) de 2\n'
      f'{len(m3)} Multiplo(s) de 3\n'
      f'{len(m4)} Multiplo(s) de 4\n'
      f'{len(m5)} Multiplo(s) de 5')
