# 2720번 세탁소 사장 동혁
T = int(input())

cnt = 0
li = []
while True:
    cnt += 1
    if cnt > T:
        break

    C = int(input())
    quo, _ = divmod(C, 25)
    C = C%25
    quo2, _ = divmod(C, 10)
    C = C%10
    quo3, _ = divmod(C, 5)
    C = C%5
    quo4, _ = divmod(C, 1)

    print(quo, quo2, quo3, quo4)