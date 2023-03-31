# 5575번 타임 카드
i = 0
while True:
    a1, a2, a3, b1, b2, b3 = map(int, input().split())

    if b3-a3 >= 0:
        if b2-a2 >= 0 :
            print(b1-a1, b2-a2, b3-a3)
        else:
            b1 -= 1
            b2 += 60
            print(b1-a1, b2-a2, b3-a3)
    else:
        b3 += 60
        b2 -= 1
        if b2-a2 >= 0:
            print(b1-a1, b2-a2, b3-a3)
        else:
            b1 -= 1
            b2 += 60
            print(b1-a1, b2-a2, b3-a3)

    i += 1
    if i > 2:
        break