# 2525번 오븐 시계

hour, minute = map(int, input().split()) # 현재 시각
time = int(input()) # 요리에 필요한 시간

if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= time <= 1000:
    if minute + time >= 60:
        a, b = divmod(minute + time, 60)
        
        if hour + a >= 24:
            c, d = divmod(hour + a, 24)
            print(d, b)

        else:
            print(hour + a, b)

    else:
        print(hour, minute + time)