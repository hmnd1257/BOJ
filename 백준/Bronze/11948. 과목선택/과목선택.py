#11948번 과목선택

a_li = []
b_li = []
i = 0
for _ in range(6):
    i += 1
    score = int(input())
    if i <= 4:
        a_li.append(score)
    else:
        b_li.append(score)

a_li.remove(min(a_li))
b_li.remove(min(b_li))

print(sum(a_li) + sum(b_li))