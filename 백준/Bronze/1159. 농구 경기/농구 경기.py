n = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha = list(alpha)

name_li = []
for _ in range(n):
    name = str(input())
    name_li.append(name[0])


alpha_li = []
for i in alpha:
    if name_li.count(i) >= 5:
        alpha_li.append(i)

# print(alpha_li)
# print(len(alpha_li))

if len(alpha_li) == 0:
    print('PREDAJA')

else:
    alpha_li.sort()
    for alpha in alpha_li:
        print(alpha, end='')