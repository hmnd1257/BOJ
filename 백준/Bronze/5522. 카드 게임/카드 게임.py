sum_li = []
for i in range(5):
    num = int(input())
    if 0 <= num <= 100:
        sum_li.append(num)
num_sum = sum(sum_li)
print(num_sum)