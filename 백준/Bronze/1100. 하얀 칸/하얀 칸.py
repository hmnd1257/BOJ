# 1110번 하얀 칸

cnt = 0
for i in range(1, 8+1):
    word = str(input())
    
    for j in range(1, len(word)+1):
        
        if (i % 2 == 0) and (j % 2 == 0): # 짝수 흰색
            if word[j-1] in 'F':
                cnt += 1
            # print('z',word[j-1])
            
        elif (i % 2 != 0) and (j % 2 != 0): # 홀수
            if word[j-1] in 'F':
                cnt += 1
            # print('zz',word[j-1])
print(cnt)