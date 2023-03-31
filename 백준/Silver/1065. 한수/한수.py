# 1065번
def hansu(N):
    if N < 100:
        cnt = N
    else:
        cnt = 99
        for i in range(100, N+1):
            n_ = list(map(int, str(i)))
            if (n_[1]-n_[0]) == (n_[2]-n_[1]):
                cnt +=1
    return cnt
a = int(input())
print(hansu(a))