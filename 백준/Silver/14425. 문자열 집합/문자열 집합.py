n, m = map(int, input().split())

s_li = set(list(str(input()) for _ in range(n)))

cnt=0
for _ in range(m):
    word = str(input())
    if word in s_li:
        cnt +=1

print(cnt)