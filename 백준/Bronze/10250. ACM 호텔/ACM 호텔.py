# 10250 ACM 호텔

case = int(input())


    
for _ in range(case):
    height, weight, num = map(int, input().split())

    a = num%height # 층수
    b = num//height + 1 # 호수

    if num%height == 0:
        a = height
        b = num//height

    print(a*100 + b)
