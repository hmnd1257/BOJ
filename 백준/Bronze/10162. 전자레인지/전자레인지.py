# 10162번 전자레인지

time = int(input())

A = time // 300
B = (time%300) // 60
C = (time%300) % 60

if (C%10) != 0:
    print('-1')
else:
    print(A, B, C//10)