# 2563번 색종이
testcase = int(input())
arr_zeros = [list([0]*100) for _ in range(100)]

cnt = 0
for _ in range(testcase):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if arr_zeros[i][j] == 0:
                arr_zeros[i][j] = 1
                cnt += 1            
print(cnt)