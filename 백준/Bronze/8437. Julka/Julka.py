a = int(input())
b = int(input())

# print((a+b)//2)
# print((a-b)//2)

if 0 <= a <= 10**100:
    # c = a//2 + b//2 ; print(c)
    d = a//2 - b//2
    x = a - d 
    print(x)
    print(d)