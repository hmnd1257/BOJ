from sys import stdin

N, K = map(int, stdin.readline().split(' '))
fK = K % 10
f2K = (2 * K) % 10
f = []

for x in range(1, N+1):
    fx = x % 10

    if fx != fK and fx != f2K:
        f.append(str(x))
        
print(len(f))
print(' '.join(f))