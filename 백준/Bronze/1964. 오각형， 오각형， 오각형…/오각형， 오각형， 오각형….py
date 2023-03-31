n = int(input())

cnt = 2
li = []
for i in range(n):
    if i > 1:    
        cnt += 3

    li.append(cnt)

li[0] = 0
result = 5 + (n-1)*5 + sum(li)

print(result%45678)