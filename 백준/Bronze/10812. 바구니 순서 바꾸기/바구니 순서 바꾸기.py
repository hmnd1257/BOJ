# 10812번 바구니 순서 바꾸기
N, M = map(int, input().split())
arr = [i+1 for i in range(N)]
for _ in range(M):
    i, j, k= map(int, input().split())
    i = i-1
    k = k-1
    begin = arr[i:k]
    end = arr[k:j]
    arr[k:j] = begin
    arr[i:k] = end
for result in arr:
    print(result, end=' ')