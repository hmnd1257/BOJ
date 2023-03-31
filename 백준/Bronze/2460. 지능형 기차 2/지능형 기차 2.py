# 2460번 지능형 기차2

li = []
calcul = 0
for _ in range(10):
    n, m = map(int, input().split())
    calcul = (calcul - n) + m
    li.append(calcul)
print(max(li))