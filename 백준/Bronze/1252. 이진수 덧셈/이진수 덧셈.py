# 1252번 이진수 덧셈

a, b = map(str, input().split())
a, b = int(a, 2), int(b, 2)

result = bin(a+b)

print(result[2:])