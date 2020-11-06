# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

meses = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

while True:
    try:
        mes, dia = map(int, input().split())

        if mes == 12 and dia == 25:
            print('E natal!')
        elif mes == 12 and dia == 24:
            print('E vespera de natal!')
        elif mes == 12 and dia > 25:
            print('Ja passou!')
        else:
            dias = 0

            for d in meses.items():
                if d[0] > mes and d[0] != 12:
                    dias += d[1]
                elif d[0] > mes and d[0] == 12:
                    dias += 25

            tot = meses.get(mes)
            dias += tot - dia

            print(f'Faltam {dias} dias para o natal!')

    except EOFError:
        break
