n, m = map(int, input().split())

import collections
n_li = list(str(input()) for _ in range(n))
m_li = list(str(input()) for _ in range(m))

n_counter = collections.Counter(n_li)
m_counter = collections.Counter(m_li)

result = []
cnt = 0
for k, v in (n_counter & m_counter).items():
    cnt += v
    result.append(k)

result.sort()
print(cnt)
for i in result:
    print(i)