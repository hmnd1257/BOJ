N = []
for i in range(10):
    a = int(input())
    b = a % 42
    N.append(b)
    
n = set(N)
print(len(n))