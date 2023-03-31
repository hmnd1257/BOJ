# 1225번 곱셈

a, b = (map(str, input().split()))
a, b = list(a), list(b)

a, b = list(map(int, a)), list(map(int, b))

print(sum(a)*sum(b))