name_length = int(input())
name = input()

name_score = 0

for alphabet in name:
    name_score += ord(alphabet) - 64

print(name_score)