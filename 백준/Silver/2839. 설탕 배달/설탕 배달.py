# 2839번 설탕 배달
num = int(input())

cnt = 0

while num >= 0:
    if num%5 == 0:
        print(num//5 + cnt)
        break
    
    num -= 3
    cnt += 1
else:
    print('-1')