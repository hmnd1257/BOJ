# 11478번 서로 다른 부분 문자열의 개수

word = str(input())
cnt = 0
result = []
while True:
    cnt += 1
    for i in range(cnt, len(word)+1, 1):
        result.append(word[cnt-1:i])
        
    if cnt == len(word):
        break
print(len(set(result)))