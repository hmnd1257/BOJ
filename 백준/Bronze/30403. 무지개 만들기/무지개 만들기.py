N = int(input())

swordList = ['r', 'o', 'y', 'g', 'b', 'i', 'v']
dwordList = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']

S = []
D = []

sSign = 0 
dSign = 0

ans = input()

for i in ans : 
    
    if i.isupper() : 
        D.append(i)
    elif i.islower() : 
        S.append(i)

if all(str in S for str in swordList) : 
    sSign = 1

if all(str in D for str in dwordList) : 
    dSign = 1

if sSign == 1 and dSign == 1 : 
    print('YeS')
elif sSign == 1 and dSign == 0 : 
    print('yes')
elif sSign == 0 and dSign == 1 : 
    print('YES')
else : 
    print('NO!')