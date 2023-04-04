N = int(input())

for i in range(N):
    i += 1
    print(" "*(N-i) + "*"*(2*i-1))
for j in range(N-1):
    j += 1
    print(" "*(j) + "*"*(2*N - (2*j+1)))