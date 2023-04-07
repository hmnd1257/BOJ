# 3009번 네 번째 점
x_li, y_li = [], []

for i in range(3):
    x, y = map(int, input().split())
    x_li.append(x)
    y_li.append(y)

for i in range(3):
    x_cnt = x_li.count(x_li[i])
    if x_cnt==1:
        x = x_li[i]
    y_cnt = y_li.count(y_li[i])
    if y_cnt==1:
        y = y_li[i]
print(x, y)