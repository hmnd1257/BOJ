import sys

def to_hms(sec):
    sec %= (24 * 3600)

    h = sec // 3600
    sec %= 3600
    m = sec // 60
    sec %= 60
    s = sec

    print(h, m, s)
    
h, m, s = map(int, sys.stdin.readline().split())
seconds = s + m * 60 + h * 3600

q = int(sys.stdin.readline())

for _ in range(q):
    T = list(map(int, sys.stdin.readline().split()))
    if T[0] == 1:
        seconds += T[1]
    elif T[0] == 2:
        seconds -= T[1]
    else:
        to_hms(seconds)