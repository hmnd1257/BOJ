# 1371번 
import sys

# word = str(input())
word = str(sys.stdin.read())
alpha_li = list('abcdefghijklmnopqrstuvwxyz')

li = []
for alpha in alpha_li:
    li.append(word.count(alpha))
    # print(word.count(alpha))

max_li = max(li)

idx_li = []
for idx, i in enumerate(li):
    if i == max_li:
        idx_li.append(idx)
        # print(idx, i)

result_li = []
for idx in idx_li:
    result_li.append(alpha_li[idx])

result_li.sort()

for result in result_li:
    print(result, end='')