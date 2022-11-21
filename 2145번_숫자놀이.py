# 2145번 숫자 놀이

while True:
    num = int(input())
    if num == 0:
        break

    while True:
        # print(list(str(num)))
        num = sum(map(int, list(str(num))))
        if num < 10:
            break
    print(num)