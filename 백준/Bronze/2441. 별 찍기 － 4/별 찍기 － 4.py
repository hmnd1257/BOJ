# 2440번 별 찍기 -3
n = int(input())
cnt = list(range(1, n+1))
# cnt.reverse()

for i in cnt:
    a = ' '*(i-1) + '*'*(n-i+1)
    
    print(a)