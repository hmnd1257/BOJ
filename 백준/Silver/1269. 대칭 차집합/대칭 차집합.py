# 1269번 대칭 차집합
a, b = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

print(len(a_set ^ b_set))