# 2914번 저작권
# x를 구하라
A, I = map(float, input().split()) # A 곡의 개수, I = 평균값, % x(저작권 멜로디 개수)/A = I

if 1 <= A and I <= 100:
    I = I - 1
    melody = A*I + 1
    print(int(melody))
