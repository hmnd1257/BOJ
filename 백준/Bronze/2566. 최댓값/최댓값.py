# 2566번 최댓값
arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

value_max = arr[0][0]
for i in range(9):
    for j in range(9):
        if value_max <= arr[i][j]:
            value_max = arr[i][j]
            idx = (i+1, j+1)
print(value_max)
print(idx[0], idx[1])