A, B, C = input().split()
A, B, C = float(A), float(B), float(C)

if C > B and C > A:
    D, F = A, C
    A, C = F, D
if B > A and B > C:
    D, F = A, B
    A, B = F, D
if B < C:
    G, H = B, C
    B, C = H, G

if A >= B + C:
    print('NAO FORMA TRIANGULO')
if A ** 2 == (B ** 2 + C ** 2) and A < B + C:
    print('TRIANGULO RETANGULO')
if A ** 2 > (B ** 2 + C ** 2) and A < B + C:
    print('TRIANGULO OBTUSANGULO')
if A ** 2 < (B ** 2 + C ** 2) and A < B + C:
    print('TRIANGULO ACUTANGULO')
if A == B == C and A < B + C:
    print('TRIANGULO EQUILATERO')
if A != B == C or B != A == C or C != A == B and A < B + C:
    print('TRIANGULO ISOSCELES')
