# 10798번 세로읽기
arr = []
cnt = 0
for _ in range(5):
    temp = list(map(str, input()))
    arr.append(temp)
    if cnt < len(temp):
        cnt = len(temp)
        
word = ''
for i in range(cnt):
    for j in range(5):
        try:
            word += arr[j][i]
        except:
            pass
print(word)