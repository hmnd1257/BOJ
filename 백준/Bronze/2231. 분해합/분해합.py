N = int(input())

found = False
for i in range(1, N+1):
    temp = sum(list(map(int, list(j for j in str(i)))))
    generator = int(i) + temp
    if generator == N:
        print(i)
        found = True
        break
if not found:
    print(0)