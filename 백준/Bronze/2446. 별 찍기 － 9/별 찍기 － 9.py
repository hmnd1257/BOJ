n = int(input())

li = []
for i in range(n):
    a = ' '*(i) + '*'*((2*n-1)-(2*i)) + ' '*(i)
    li.append(a)

for i in li:
    i = i.rstrip(' ')
    print(i)

b = li[::-1]
del b[0]

for i in b:
    i = i.rstrip(' ')
    print(i)