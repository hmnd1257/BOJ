# 9506번 약수들의 합
while True:
    N = int(input())
    if N == -1:
        break
        
    li = []
    value = 0
    for i in range(1, N+1):
        if N%i ==0:
            if i != N:
                li.append(i)
                
    li = sorted(li)

    if sum(li) == N:
        print(N, " = ", " + ".join(str(i) for i in li), sep="")
    else:
        print(f'{N} is NOT perfect.')