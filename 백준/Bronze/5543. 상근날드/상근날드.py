# 5543번 상근날드

burger = []
drink = []

cnt = 0
for _ in range(5):
    cnt += 1
    if cnt < 4:
        burger.append(int(input()))
    else:
        drink.append(int(input()))

li = []
for i in burger:
    for j in drink:
        result = i + j
        li.append(result-50)
print(min(li))