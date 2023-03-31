# 3046번 R2

R1, S = map(int, input().split())

if -1000 <= R1 <= 1000 and -1000 <= S <= 1000:
    R2 = (2*S) - R1
    print(R2)