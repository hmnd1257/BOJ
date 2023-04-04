grade_li = {'A+': 4.5,
            'A0': 4.0,
            'B+': 3.5,
            'B0': 3.0,
            'C+': 2.5,
            'C0': 2.0,
            'D+': 1.5,
            'D0': 1.0,
            'F': 0.0}

result = 0
total_score = 0
for i in range(20):
    _, score ,grade = map(str, input().split())
    if grade == 'P':
        continue
    total_score += float(score)
    result += float(score)*grade_li[grade]

result = result/total_score
print(f'{result:.6f}')