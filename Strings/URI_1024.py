def criptografia(lista):
    # Primeiro deslocar 3 posições as letras maiusuclas e minusculas para direita.
    aux = [c+3 if 65 <= c <= 90 or 97 <= c <= 122 else c for c in lista]

    # A linha deve ser invertida.
    aux = aux[::-1]

    # Deslocar uma posição da metade truncada em diante para a esquerda.
    metade = len(aux) // 2
    codificado_unicode = [aux[c] - 1 if c >= metade else aux[c] for c in range(len(aux))]
    codificado_ascii = [chr(c) for c in codificado_unicode]

    return ''.join(codificado_ascii)


vezes = int(input())
for v in range(vezes):
    mensagem = input().strip()

    unicode = [ord(l) for l in mensagem]
    crip = criptografia(unicode)
    print(crip)
