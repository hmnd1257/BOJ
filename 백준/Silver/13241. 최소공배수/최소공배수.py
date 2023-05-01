# 13241번 최소공배수 (유클리드 호제법)
def gcd(a, b):
    if b==0:
        return a
    a = a%b
    return gcd(max(a,b), min(a,b))

def lcm(a,b):
    return (a*b) // gcd(a,b)

a, b = map(int, input().split())
print(lcm(a, b))