n = int(input())

def sum_n(n):
    j = 0
    for i in range(1,n+1):
        j += i
    return j 

print(sum_n(n))