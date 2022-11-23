li = []
for i in range(5):
    a, b, c, d = map(int, input().split())
    value = a+b+c+d

    li.append(value)
# print(li)
print(li.index(max(li))+1, end=' ')
print(max(li))
