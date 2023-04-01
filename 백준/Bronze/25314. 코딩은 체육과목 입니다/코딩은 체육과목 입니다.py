# 25314 코딩은 체육과목 입니다
N = int(input())
word = []
if N%4 == 0:
    for i in range(N//4):
        word.append('long')
for j in word:
    print(j, end=' ')
print('int')