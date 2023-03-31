D, H, M = map(int, input().split())
temp = 11*60*24 + 11*60 + 11
temp2 = D*60*24 + H*60 + M

t = temp2 - temp
if t < 0:
    print('-1')
else:
    print(t)