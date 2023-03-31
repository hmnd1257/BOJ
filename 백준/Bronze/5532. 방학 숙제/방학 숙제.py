# 5532번 방학 숙제

L = int(input()) # 방학
A = int(input()) # 국어 총 페이지
B = int(input()) # 수학 총 페이지
C = int(input()) # 국어 하루 최대
D = int(input()) # 수학 하루 최대

if (A%C) == 0:
    a = (A//C)
else:
    a = (A//C) + 1

if (B%D) == 0:
    b = (B//D)
else:
    b = B//D + 1

print(L - max(a,b))