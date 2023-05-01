def gcd(a, b):
    if b==0:
        return a
    a = a%b
    return gcd(max(a,b), min(a,b))

def lcm(a,b):
    return (a*b) // gcd(a,b)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a, b))