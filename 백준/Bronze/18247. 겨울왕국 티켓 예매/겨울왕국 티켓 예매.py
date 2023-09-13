T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    
    if M < 4 or N < 12: #L4자리가 없는 경우
        print(-1)
    else:
        print(11 * M + 4)