A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

x_company = P*A

if P <= C:
    y_company = B
else:
    y_company = B + ((P-C)*D)

print(min(x_company, y_company))