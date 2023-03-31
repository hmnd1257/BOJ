# 5893번 17배
N = int(input())
N = int(str(N), 2)
N = N*17
answer = bin(N) ; print(answer[2:])