
N, M = map(int, input().split())
arr = [0 for i in range(N)]

for i in range(M):
    i, j, k = map(int, input().split())
    i = i-1
    k_li = [k for _ in range(j-i)]
    arr[i:j] = k_li

for result in arr:
    print(result, end=' ')