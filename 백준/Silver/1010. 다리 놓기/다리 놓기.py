# 1010번 다리 놓기
import math

testcase = int(input())

i = 0
while True:
    i = i + 1
    if i > testcase:
        break

    n, m = map(int, input().split())
    if 0 < n <= m < 30:
        result = (math.factorial(m)//math.factorial(m-n)) // math.factorial(n)
        print(int(result))