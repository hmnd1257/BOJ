# 2355번 시그마

a, b = map(int, input().split())
if a>b:
    a,b = b,a
a_sum = (a*(a-1))//2
b_sum = (b*(b+1))//2
print(b_sum - a_sum)