import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
l = list(map(int, input().split()))

res = 0  # 랄파와 사이가 좋지 않은 스트리머 수
for _ in range(n-1):
    k = list(map(int, input().split()))
    diff = 0
    for i in range(m):
        diff += abs(l[i] - k[i])

    if diff > 2000:
        res += 1

# 절반 이상이 좋지 않은 스트리머라면 악성 시청자
if n-1 <= res*2:
    print("YES")
else:
    print("NO")