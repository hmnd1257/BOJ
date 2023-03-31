n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]

for i in arr:
    cnt = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            cnt +=1
    print(cnt)
        # print(i[0], i[1], "d", j[0], j[1])
        # print(i, j)