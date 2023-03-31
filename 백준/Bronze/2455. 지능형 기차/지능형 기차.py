li = []
calcul = 0
for _ in range(4):
    n, m = map(int, input().split())
    calcul = (calcul - n) + m
    li.append(calcul)
print(max(li))