N = int(input())

li = list(map(int, input().split()))
li_dict = {}

for idx, value in enumerate(sorted(set(li))):
    li_dict[value] = idx

for i in range(N):
    print(li_dict.get(li[i]), end=' ')