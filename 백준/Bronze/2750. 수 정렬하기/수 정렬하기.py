N = int(input())
N_li = list(int(input()) for i in range(N))
N_li.sort(key=int)

for value in N_li:
    print(value)