testCase = int(input())
b = str('O')
c = str('X')

for i in range(testCase):
    a = str(input())
    
    score = 0
    cnt = 0
    for j in range(len(a)):
        if a[j] == b:
            cnt += 1
            score += cnt
        elif a[j] == c:
            cnt = 0
            score += cnt

    print(score)