g_inter = g_gremio = grenais = empates = 0
while True:
    inter, gremio = map(int, input().split())

    grenais += 1
    g_inter += 1 if inter > gremio else 0
    g_gremio += 1 if inter < gremio else 0
    empates += 1 if inter == gremio else 0

    print('Novo grenal (1-sim 2-nao)')
    resp = int(input())
    if resp == 2:
        if g_inter > g_gremio:
            vencedor = 'Inter venceu mais'
        elif g_gremio > g_inter:
            vencedor = 'Gremio venceu mais'
        else:
            vencedor = 'Nao houve vencedor'
        break
print('{} grenais\n'
      'Inter:{}\n'
      'Gremio:{}\n'
      'Empates:{}\n'
      '{}'.format(grenais, g_inter, g_gremio, empates, vencedor))
