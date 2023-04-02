all_students = set(range(1, 31))

for _ in range(28):
    n = int(input())
    all_students.remove(n)

missing_students = sorted(list(all_students))

print(min(missing_students))
print(max(missing_students))