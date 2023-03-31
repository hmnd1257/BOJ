# 2526번 싸이클

N, P = map(int, input().split())

result = N
li = [N]

while True:
    result = (result*N)%P
    if result not in li:
        li.append(result)
    else:
        break

for i in range(len(li)):
    if li[i] == result:

        break
print(len(li) - i)