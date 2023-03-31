# 4299번 AFC 윔블던
a, b = map(int, input().split()) # a=합, b=차


if a+b < 0 or a-b < 0 or a < b or (a + b) % 2:
    print('-1')
else:
    y = (a-b)//2
    x = a-y
    print(max(x, y), min(x, y))
