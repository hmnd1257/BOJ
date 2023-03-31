# 2475번 검증수

def calculation(a1, a2, a3, a4, a5):
    a1 = a1**2
    a2 = a2**2
    a3 = a3**2
    a4 = a4**2
    a5 = a5**2
    calcul = a1 + a2 + a3 + a4 + a5
    result = calcul%10
    return result
    
a1, a2, a3, a4, a5 = map(int, input().split())
result = calculation(a1, a2, a3, a4, a5)
print(result)