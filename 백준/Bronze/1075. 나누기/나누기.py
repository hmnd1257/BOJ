# 1075번 나누기

a = str(input())
b = int(input())

li = []
a_new = (a[:-2])
for i in range(100):
    if i < 10:
        temp = a_new + '0' + str(i)
    else:
        temp = a_new + str(i)
    
    if int(temp) % b == 0:
        li.append(temp)
print(min(li)[-2:])