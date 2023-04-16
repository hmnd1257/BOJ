# 2587번 대표값2
value_li = list(int(input()) for _ in range(5))
value_li.sort(key=int)

print(sum(value_li)//len(value_li), value_li[2])