N = int(input())
cards = set(map(int, input().split()))

M = int(input())
check_values = list(map(int, input().split()))

result = [1 if value in cards else 0 for value in check_values]
print(" ".join(map(str, result)))