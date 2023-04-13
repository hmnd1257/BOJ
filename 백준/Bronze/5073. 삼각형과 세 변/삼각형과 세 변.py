while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    
    li = [a, b, c]
    
    if max(li) >= sum(li) - max(li):
        print('Invalid')
    else:
        cnt = 0
        if li[0] == li[1]:
            cnt += 1
        if li[0] == li[2]:
            cnt += 1
        if li[1] == li[2]:
            cnt += 1
        
        print('Equilateral' if cnt == 3 else ('Isosceles' if cnt == 1 else 'Scalene'))