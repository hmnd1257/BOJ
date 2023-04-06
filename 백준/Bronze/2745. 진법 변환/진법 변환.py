# 2745번 진법 변환
N, B = map(str, input().split())
N, B = N[::-1], int(B)
word = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = 0
for i in reversed(range(len(N))):    
    result += word.index(N[i])*(B**i)
print(result)