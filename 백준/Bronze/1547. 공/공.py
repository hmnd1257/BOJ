# 1547번 공

n = int(input())
li = ['1', '2', '3']

for _ in range(n):
    x, y = map(int, input().split())

    temp = li[x-1]
    li[x-1] = li[y-1]
    li[y-1] = temp
    
print(li.index('1')+1)