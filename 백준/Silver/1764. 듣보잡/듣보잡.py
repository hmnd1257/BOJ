from collections import Counter

n, m = map(int, input().split())
n_li = [input() for _ in range(n)]
m_li = [input() for _ in range(m)]

common = sorted((Counter(n_li) & Counter(m_li)).elements())

print(len(common))
print("\n".join(common))