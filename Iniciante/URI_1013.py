numbers = str(input()).split()
a, b, c = int(numbers[0]), int(numbers[1]), int(numbers[2])
maior = (a + b + abs(a - b)) // 2
maior_c = (maior + c + abs(maior - c)) // 2
print('{} eh o maior'.format(maior_c))
