# 1212번 8진수 2진수
n = input()
n = int(n, 8)

n = bin(n)
print(str(n)[2:])