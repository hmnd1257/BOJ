n = int(input())
call_time = list(map(int, input().split()))


y_li, m_li = [], []
for i in range(n):
    y = m = 0
    y += ((call_time[i]//30) + 1)*10
    y_li.append(y)
    m += ((call_time[i]//60) + 1)*15
    m_li.append(m)

y = sum(y_li)
m = sum(m_li)
if y > m:
    print('M', m)
elif y < m:
    print('Y', y)
else:
    print('Y', 'M', min(y, m))