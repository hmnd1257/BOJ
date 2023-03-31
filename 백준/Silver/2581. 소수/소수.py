# 2581번 소수

a = int(input())
b = int(input())

li = list(range(a, b+1))
# print(li)

answer = []
for i in li:
    result = 1
    for j in range(2, i):
        if i%j == 0:
            result = 0
    if result == True:
        if not i == 1:
            answer.append(i)

if bool(answer) == True:
    print(sum(answer))
    print(min(answer))
else:
    print('-1')