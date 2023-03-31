#1703번 생장점

while True:
    temp = list(map(int, input().split()))

    if temp[0] == 0:
        break
        
    leaf = 1
    if temp[0] == 1:
        leaf = leaf*temp[1] - temp[2]
        print(leaf)
    else:
        for i in range(1, temp[0]+1):
            leaf = leaf*temp[(i*2)-1] - temp[i*2]
        print(leaf)