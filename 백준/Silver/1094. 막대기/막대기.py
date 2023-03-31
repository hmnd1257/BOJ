# 1094번 막대기

x = int(input())
n_li = [64, 32, 16, 8, 4, 2, 1]

li = [n_li[i] for i in range(len(n_li)) if n_li[i] <= x]
# print(li)

a = 0
cnt = 0
for i in li:
    # a += i
    if a+i <= x:
        a += i
        cnt += 1
        
print(cnt)