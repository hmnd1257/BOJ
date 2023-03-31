alp = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = str(input())

time = 0
for i in alp:
    for j in i:
        for x in word:
            if j == x :
                time += alp.index(i)+3 
print(time)