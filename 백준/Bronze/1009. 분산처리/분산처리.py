# 1009번 분산처리

case = int(input())
for _ in range(case):
    a, b = map(int, input().split())
    a = a%10
    if a==1 or a==5 or a==6:
        print(a)
    elif a==4 or a==9:
        if b%2 == 0:
            print(str(a**2)[-1])
        else:
            print(a)
    elif a==2 or a==3 or a==7 or a==8:
        if b%4 == 0:
            temp = a**4
            print(str(temp)[-1])
        else:
            temp =a**((b%4)) 
            print(str(temp)[-1])
    else:
        print('10')