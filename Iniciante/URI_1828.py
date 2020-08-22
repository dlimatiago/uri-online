# from Teste.Testador import Testes
# t = Testes('C:/Users/Tiago/PycharmProjects/URIonline/Teste/Respostas.txt')

tent = int(input())
for k in range(1, tent + 1):
    # Pedra-Papel-Tesoura-Lagarto-Spock
    sheldon, raj = map(lambda x: str(x).lower()[:2], input().split())

    if raj == sheldon:
        print(f'Caso #{k}: De novo!')
        continue
    if raj == 'te' or sheldon == 'te':
        if raj in ['pe', 'sp']:
            print(f'Caso #{k}: Raj trapaceou!')
            continue
        elif sheldon in ['pe', 'sp']:
            print(f'Caso #{k}: Bazinga!')
            continue
    if raj == 'pe' or sheldon == 'pe':
        if raj in ['pa', 'sp']:
            print(f'Caso #{k}: Raj trapaceou!')
            continue
        elif sheldon in ['pa', 'sp']:
            print(f'Caso #{k}: Bazinga!')
            continue
    if raj == 'pa' or sheldon == 'pa':
        if raj in ['te', 'la']:
            print(f'Caso #{k}: Raj trapaceou!')
            continue
        elif sheldon in ['te', 'la']:
            print(f'Caso #{k}: Bazinga!')
            continue
    if raj == 'la' or sheldon == 'la':
        if raj in ['pe', 'te']:
            print(f'Caso #{k}: Raj trapaceou!')
            continue
        elif sheldon in ['pe', 'te']:
            print(f'Caso #{k}: Bazinga!')
            continue
    if raj == 'sp' or sheldon == 'sp':
        if raj in ['la', 'pa']:
            print(f'Caso #{k}: Raj trapaceou!')
            continue
        elif sheldon in ['la', 'pa']:
            print(f'Caso #{k}: Bazinga!')
            continue
