a, b, c = map(int, input().split())
s1, s2, s3 = list(range(1, a+1)), list(range(1, b+1)), list(range(1, c+1))

li = []
for i in s1:
    for j in s2:
        for z in s3:
            li.append(i+j+z)

cnt_li = []
for i in range(1, max(li)+1):
    cnt_li.append(li.count(i))
    # print(i)
# print(cnt_li)
print(cnt_li.index(max(cnt_li))+1)