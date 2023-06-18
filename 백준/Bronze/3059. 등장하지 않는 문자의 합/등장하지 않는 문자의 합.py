import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  alphabet = [0] * 27
  value = input().rstrip()
  for i in range(len(value)):
    alphabet[int(ord(value[i])) - 65] += 1

  result = 0
  for i in range(26) :
    if alphabet[i] == 0 :
      result += i + 65

  print(result)