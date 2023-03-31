# 1284번 집 주소

while True:
    a = str(input())
    if a == '0':
        break

    result = 0
    for i in range(len(a)):
        if a[i] == '0':
            result += 4
            # print('1: ', result)
        elif a[i] == '1':
            result += 2
            # print('2: ', result)
        else:
            result += 3
            # print('3: ', result)

    result += 1*(len(a)+1)

    print(result)