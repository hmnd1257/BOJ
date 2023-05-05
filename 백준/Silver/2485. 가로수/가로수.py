# 2485번 가로수
def gcd(a, b):
    if b==0:
        return a
    a = a%b
    return gcd(max(a,b), min(a,b))

N = int(input())

trees = [int(input()) for _ in range(N)]

gaps = [trees[i] - trees[i-1] for i in range(1, N)]

gaps_set = list(set(gaps))

temp = gaps_set[0]
for i in range(1, len(gaps_set)):
    temp = gcd(temp, gaps_set[i])

result = ((max(trees)-min(trees)) // temp) + 1 - len(trees)

print(result)