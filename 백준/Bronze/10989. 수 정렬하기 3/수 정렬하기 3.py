# 2750번 수 정렬하기기
import sys
input = sys.stdin.readline

arr = [0]*10001
N = int(input())

for _ in range(N):
    arr[int(input())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)