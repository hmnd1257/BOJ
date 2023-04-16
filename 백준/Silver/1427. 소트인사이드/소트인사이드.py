value = str(input())
arr = [0]*11
# print(arr)
for idx in value:
    arr[int(idx)] += 1
# print(arr)

for i in reversed(range(11)):
    if arr[i] != False:
        for j in range(arr[i]):
            print(i, end='')