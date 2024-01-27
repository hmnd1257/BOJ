N = int(input())
nameList = []


for i in range(N) : 
    name = input()
    
    if len(name) == 3 : 
        nameList.append(name)

nameList.sort()

print(nameList[0])