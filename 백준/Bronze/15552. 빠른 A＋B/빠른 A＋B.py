import sys

test_case = int(input())

for i in range(1, test_case + 1):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)