N = int(input())

for i in range(1,N+1):
    star = (N-i)
    star_ = '*'
    print(' '*int(star), star_*i, sep='')