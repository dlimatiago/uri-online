p1, p2, p3 = input().strip(), input().strip(), input().strip()

if p1 in 'vertebrado':
  if p2 in 'ave':
    if p3 in 'carnivoro':
      print('aguia')
    if p3 in 'onivoro':
      print('pomba')
  if p2 in 'mamifero':
    if p3 in 'herbivoro':
      print('vaca')
    if p3 in 'onivoro':
      print('homem')
if p1 in 'invertebrado':
  if p2 in 'inseto':
    if p3 in 'hematofago':
      print('pulga')
    if p3 in 'herbivoro':
      print('lagarta')
  if p2 in 'anelideo':
    if p3 in 'hematofago':
      print('sanguessuga')
    if p3 in 'onivoro':
      print('minhoca')
