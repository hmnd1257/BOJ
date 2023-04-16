from collections import Counter

N = int(input())
card_values = list(map(int, input().split()))

M = int(input())
check_values = list(map(int, input().split()))

counter = Counter(card_values)

result = [counter[value] if value in counter else 0 for value in check_values]
print(" ".join(map(str, result)))