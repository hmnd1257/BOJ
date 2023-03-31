N = int(input())
a = N

cnt = 0
while True:
    if 0 <= N <= 99:              # N이 10보다 작을 경우 십의 자리로 만듦
        n = ((((N//10) + (N%10))%10) + ((N%10)*10))
        cnt += 1
    # else:
    #     n = ((((N//10) + (N%10))%10) + ((N%10)*10))
    #     cnt += 1
    if a == n:
        break
    N=n

print(cnt)