# 2490번 윷놀이

i = 0
while True:
    i += 1
    if i > 3:
        break

    li = list(map(int, input().split()))
    a = li.count(1) # 등
    b = li.count(0) # 배
    
    if a == 3 and b == 1: # 도
        print('A')
    elif a == 2 and b == 2: # 개
        print('B')
    elif a == 1 and b == 3: # 걸
        print('C')
    elif a == 0 and b == 4: # 윷
        print('D')
    elif a == 4 and b == 0: # 모
        print('E')