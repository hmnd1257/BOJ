N, M = map(int, input().split())
li= list(map(int, input().split()))

max_value = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            li_sum = li[i]+li[j]+li[k]
            if li_sum > M:
                continue
            else:
                if max_value < li_sum:
                    max_value = li_sum
print(max_value)