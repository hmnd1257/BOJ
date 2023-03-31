a, b, c = map(int, input().split())
if 50 <= a <= 200 and 50 <= b <= 200 and 50 <= c <= 200:
    C4, A3, A4, = 74.196, 124.74, 62.37
    result = a*2*C4 + b*2*A3 + c*A4
    print(round(result/1000, 7))
    # 120 90 70