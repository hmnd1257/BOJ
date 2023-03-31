x, y = map(int,input().split())

a = [True]*(y+1)
a[1] = False

for i in range(2, int(y**0.5)+1):
  if a[i]:
    for j in range(i*i, y+1, i):
        a[j] = False

for idx in range(x, y+1):
    if a[idx]:
        print(idx)