import sys
input = sys.stdin.readline

N, M = map(int, input().split())

N_dict = {}
for idx in range(1, N+1):
    name = str(input().strip())
    N_dict[name] = idx
    N_dict[idx] = name

for _ in range(M):
    temp = input().strip()
    if temp.isnumeric():
        print(N_dict[int(temp)])
    else:
        print(N_dict[temp])