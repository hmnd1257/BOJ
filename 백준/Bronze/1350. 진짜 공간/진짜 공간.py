# 1350번 진짜 공간

n = int(input())
size_li = list(map(int, input().split()))
cluster = int(input())

cnt = 0
for size in size_li:
    if (size%cluster == 0):
        if not (size == 0):
            cnt += size//cluster
            # print("1:", cnt)
    else:
        if size <= cluster:
            if not (size == 0):
                cnt += 1
                # print("z:", cluster*cnt)
        else:
            cnt += (size//cluster+1)
            # print("2:", cnt)
print(cluster*cnt)