# 10811번 바구니 뒤집기
N, M = map(int, input().split())
arr = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    i = i-1
    arr_slicing = arr[i:j]
    arr_slicing = arr_slicing[::-1]

    arr[i:j] = arr_slicing
for result in arr:
    print(result, end=' ')