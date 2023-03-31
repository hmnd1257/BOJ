#13866번 팀 나누기

a, b, c, d = map(int, input().split())

x, y = a+d, b+c
print(max(x, y) - min(x, y))