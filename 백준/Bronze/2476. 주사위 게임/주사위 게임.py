n = int(input())

li = []
for _ in range(n):
    a, b, c = map(int, input().split())

    if a == b and a == c and b == c:
        li.append(10000+a*1000)
    elif (a == b and b != c) or (b == c and a != b) or (a == c and b != c):
        if (a == b and b != c):
            li.append(1000+a*100)
        elif (b == c and a != b):
            li.append(1000+b*100)
        elif (a == c and b != c):
            li.append(1000+a*100)
    else:
        li.append(max(a, b, c)*100)

print(max(li))