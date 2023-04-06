N, B = map(int, input().split())

word = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

result = ''
while True:
    result += word[N%B]
    N = N//B
    if N == 0:
        break
print(result[::-1])