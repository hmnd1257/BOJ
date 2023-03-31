n = int(input())
n_li = list(map(int, input().split()))

answer = []
cnt = 0
for i in n_li:
    result = 1
    for j in range(2, i):
        if i%j == 0:
            result = 0
    if result == True:
        if not i == 1:
            answer.append(i)
    
# print(answer)
print(len(answer))