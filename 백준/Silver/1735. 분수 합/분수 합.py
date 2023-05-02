# 1735번 분수 합
def gcd(a, b):
    if b==0:
        return a
    a = a%b
    return gcd(max(a,b), min(a,b))

def lcm(a,b):
    return (a*b) // gcd(a,b)

a, b = map(int, input().split())
c, d = map(int, input().split())

numerator = a*(lcm(b, d)//b) + c*(lcm(b, d)//d)
denominator = lcm(b, d)
print(numerator//gcd(numerator,denominator), denominator//gcd(numerator,denominator))