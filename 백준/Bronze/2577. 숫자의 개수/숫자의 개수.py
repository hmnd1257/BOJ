A = int(input())
B = int(input())
C = int(input())

mul = A*B*C
mul_str = str(mul)

list = ['0','1','2','3','4','5','6','7','8','9']

print(mul_str.count(list[0])) # 1
print(mul_str.count(list[1])) # 1
print(mul_str.count(list[2])) # 2
print(mul_str.count(list[3])) # 3
print(mul_str.count(list[4])) # 4
print(mul_str.count(list[5])) # 5
print(mul_str.count(list[6])) # 6
print(mul_str.count(list[7])) # 7
print(mul_str.count(list[8])) # 8
print(mul_str.count(list[9])) # 9