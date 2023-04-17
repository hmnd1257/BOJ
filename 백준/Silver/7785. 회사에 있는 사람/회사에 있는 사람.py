# 7785번 회사에 있는 사람
from collections import Counter
n = int(input())
stay_li = []

for _ in range(n):
    name, stay = map(str, input().split())
    stay_li.append(name)

counter = Counter(stay_li)

value_li = []
for k, v in counter.items():
    if v % 2 != 0:
        value_li.append(k)

for i in sorted(value_li, reverse=True):
    print(i)