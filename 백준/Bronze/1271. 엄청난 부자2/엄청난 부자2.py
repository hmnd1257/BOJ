# 1271번 엄청난 부자2

n, m = map(int, input().split()) # n = 가진 돈, m = 생명체 수

a = n%m # 나머지
b = n//m
print(b); print(a)