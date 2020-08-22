t1, t2, t3 = map(int, input().split())
if min((t1, t2, t3)) > 0:
    media = int(t1 + t3) // 2

    if media > t2:
        print(':)')
    elif media <= t2:
        print(':(')
else:
    m1 = t2 - t1
    m2 = t3 - t2

    if m2 > m1:
        print(":)")

    elif m2 < m1:
        print(":(")

    else:
        if m1 <= 0:
            print(":(")
        else:
            print(":)")
