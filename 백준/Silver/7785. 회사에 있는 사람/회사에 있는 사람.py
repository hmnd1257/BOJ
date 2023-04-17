# 7785번 회사에 있는 사람
from collections import Counter

n = int(input())
stay_li = [input().split()[0] for _ in range(n)]

counter = Counter(stay_li)

value_li = []
for k, v in counter.items():
    if v % 2 != 0:
        value_li.append(k)

for i in sorted(value_li, reverse=True):
    print(i)