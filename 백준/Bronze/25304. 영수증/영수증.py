X = int(input())
N = int(input())

total = 0
for i in range(N):
    a, b = map(int, input().split())
    total += a*b
print('Yes') if X == total else print('No')