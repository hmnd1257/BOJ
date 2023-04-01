N = int(input())
N_li = list(map(int, input().split()))
v = int(input())

cnt = sum(1 for i in range(N) if N_li[i] == v)
print(cnt)