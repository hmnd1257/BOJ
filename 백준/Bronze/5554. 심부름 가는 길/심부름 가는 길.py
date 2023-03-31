# 5554번 심부름 가는 길

# 집 -> 학교 -> PC방 -> 학원 -> 집

li = []
for i in range(4):
    minutes = int(input())
    li.append(minutes)
x, y = divmod(sum(li), 60)
print(x)
print(y)