a = list(map(int, input().split()))
li = []
for i in range(len(a)):
    x = a[i]*5
    li.append(x)
print(sum(li))