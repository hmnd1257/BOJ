n = int(input())
while n > 0 :
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))
    n -= 1