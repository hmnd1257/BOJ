x, y = map(int, input().split())

x -= 1
y -= 1

a = y//4 - x//4
b = y%4 - x%4
print(abs(a)+abs(b))