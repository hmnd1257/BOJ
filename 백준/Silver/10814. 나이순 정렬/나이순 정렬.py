# 10814번 나이순 정렬
N = int(input())

li = [tuple(input().split()) for _ in range(N)]
li = [(int(age), name) for age, name in li]

li.sort(key=lambda x : x[0])

for x, y in li:
    print(x,y)