# 5596번 시험 점수
a = list(map(int, input().split()))
b = list(map(int, input().split()))
S, T = sum(a), sum(b)
if S == T:
    print(S)
else:
    print(max(S, T))