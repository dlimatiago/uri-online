num, den = map(int, input().split())
try:
    r = num % abs(den)
except:
    pass
else:
    q = int((num - abs(r)) / den)
    print(q, r)
