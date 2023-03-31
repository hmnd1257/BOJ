# 2775번 부녀회장이 될테야

testcase = int(input())

for _ in range(testcase):
    k = int(input()) # 층수
    n = int(input()) # 호수
    zero_floor = list(range(1, n+1)) # 0층

    for _ in range(k):
        for idx in range(1, n):
            zero_floor[idx] = zero_floor[idx] + zero_floor[idx-1]
    print(zero_floor[-1])