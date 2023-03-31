# 2609번 최대공약수와 최소공배수

def max_cnt(cnt, a, b):
    while True:
        cnt += 1
        if cnt%a == 0 and cnt%b == 0:
            max_cnt = cnt
            break
    min_cnt = (a*b)//max_cnt
    return max_cnt, min_cnt

if __name__ == '__main__':

    a, b = map(int, input().split())
    cnt = 0

    max_cnt, min_cnt = max_cnt(cnt, a, b)
    print(min_cnt, max_cnt, sep='\n')