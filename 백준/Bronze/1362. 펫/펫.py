count = 0

while True:
    count += 1
    death = 0
    o, w = map(int, input().split())
    
    if o == 0 and w == 0:
        break
    
    while True:
        ef, n = input().split()
        if ef == '#' and n == '0':
            break
        n = int(n)
        if ef == 'E':
            w -= n
        else:
            w += n
        if w <= 0:
            death = 1

    print(count, end = " ")
    if death == 1:
        print("RIP")
    else:
        if w > o/2 and w < o*2:
            print(":-)")
        else:
            print(":-(")