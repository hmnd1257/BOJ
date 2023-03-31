# 1037번 약수
# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
# N이 A의 배수 = N % A == 0

N = int(input()) # N <= 50 진짜 약수의 개수

num = map(int, input().split())
num = sorted(num)

if N == 1:
    if not num == 0:
        print(num[0]**2)
else:
    result = num[0] * num[-1]
    print(result)