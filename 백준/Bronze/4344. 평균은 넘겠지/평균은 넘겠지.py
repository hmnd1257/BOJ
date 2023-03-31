import sys

# 평균은 넘겠지
C = int(sys.stdin.readline())
case = []
a = 0
for i in range(C):
    case.append(list(map(int, sys.stdin.readline().split())))

for ii in range(C):
    obj = case[ii]
    count = int(obj[0])
    SUM = sum(obj) - count
    mean = SUM/count
    for iii in range(1, len(obj)):
        score = obj[iii]
        if mean < score:
            a = a + 1
            N = round(a / count * 100, 3)
        else:
            N = round(a / count * 100, 3)
    print("{:.3f}%".format(N))
    a = 0