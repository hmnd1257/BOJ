# 14215번 세 막대
a, b, c = map(int, input().split())
li = [a,b,c]
li.sort()
if li[0] == li[1] == li[2]:
    print(sum(li))
else:
    if li[2] >= sum(li)-li[2]:
        li[2] = sum(li)-li[2]-1
    print(sum(li))