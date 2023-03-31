# 2845번 파티가 끝나고 난 뒤

L, P = map(int, input().split()) # L = 1m^2당 사람수, P = 공간 넓이
a1, a2, a3, a4, a5 = map(int, input().split())
li = [a1, a2, a3, a4, a5]

if 1 <= L <= 10 and 1 <= P <= 1000:
    person = L * P
    
    result_li = []
    for i in range(len(li)):
        result = li[i] - person
        result_li.append(result)
    for j in range(len(result_li)):
        print(result_li[j], end=' ')