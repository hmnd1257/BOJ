n = int(input())
new_num = ""

for i in range(1, n+1):
    new_num += str(i)
# print(new_num)
print(new_num.index(str(n)) + 1)