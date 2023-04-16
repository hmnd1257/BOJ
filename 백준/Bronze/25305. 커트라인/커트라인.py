# 25305번 커트라인

N, k = map(int, input().split())
score_li = list(map(int, input().split()))

score_li.sort(key=int)
print(score_li[-k])