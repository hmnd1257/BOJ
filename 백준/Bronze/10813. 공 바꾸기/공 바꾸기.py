N, M = map(int, input().split())
arr = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    i, j = i - 1, j - 1
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

for result in arr:
    print(result, end=' ')