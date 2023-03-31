n = 999999
temp = [False,False] + [True]*(n)

primes=[]
for i in range(2, n+1):
  if temp[i]:
    primes.append(i)
    for j in range(2*i, n+1, i): 
        temp[j] = False

while True:
    case = int(input())
    if case == 0:
        break
    li = []
    for idx in range(len(primes)):
        if case < primes[idx] <= 2*case:
            li.append(primes[idx])
    print(len(li))