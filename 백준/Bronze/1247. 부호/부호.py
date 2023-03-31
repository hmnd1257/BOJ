
cnt = 0
while True:
    cnt += 1
    if cnt > 3:
        break

    N = int(input())
    S = 0
    for _ in range(N):
        S += int(input())

    if S > 0:
        print('+')
    elif S < 0:
        print('-')
    else:
        print('0')