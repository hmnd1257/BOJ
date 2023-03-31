# 11653번 소인수분해

n = int(input())
n_li = list(range(2, n+1))
# print(n_li)

li = []
while True:
    if n == 1:
        break

    for i in range(len(n_li)):
        if n%n_li[i] == 0:
            n = n//n_li[i]
            li.append(n_li[i])
            # print(n)
            break
for result in li:
    print(result)
# print(li)