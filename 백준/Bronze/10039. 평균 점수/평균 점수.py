# 10039번 평균 점수

score_li = []
for i in range(5):
    score = int(input())
    if score >= 40:
        score_li.append(score)
    else:
        a = 40
        score_li.append(a)

score_mean = sum(score_li) // len(score_li)
print(score_mean)