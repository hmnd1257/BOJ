n = int(input())

temp = list(map(int, input().split()))

cnt = 0
score = []
for i in range(n):
    if temp[i] == 1:
        cnt += 1
        score.append(cnt)
    else:
        cnt = 0
        score.append(cnt)

print(sum(score))