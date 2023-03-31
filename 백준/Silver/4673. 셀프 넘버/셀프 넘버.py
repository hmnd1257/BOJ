def self_number(n):
    next = n
    for i in list(str(n)):
        n += int(i)
    return n

con = []
for j in range(10001):
    con.append(self_number(j))

con.sort()

for j in range(1,10000):
    if j in con:
        pass
    else:
        print(j)