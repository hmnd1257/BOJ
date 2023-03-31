# 1059번 좋은 구간

L = int(input())
s_li = list(map(int, input().split()))
s_li = [0] + s_li
s_li.sort()

# print(s_li)
n = int(input())

cnt = 0
for i in range(L):
    if n in s_li:
        cnt = 0
    elif s_li[i] < n and n < s_li[i+1]:
        a = list(range(s_li[i]+1, s_li[i+1]))
        # print(a)
        for j in a:
            for z in a:
                if j < z:
                    if j <= n <= z:
                        # print(j, z)
                        cnt += 1
        

print(cnt)