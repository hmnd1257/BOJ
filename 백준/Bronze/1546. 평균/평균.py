N = int(input())
grade = list(map(int, input().split()))

maxGrade = max(grade)
MaxGrade = maxGrade*100

new_grade = []
for i in range(len(grade)):
    new_Grade = ((grade[i])/(MaxGrade))
    new_grade.append(new_Grade)
    average = sum(new_grade)/N
    Average = float((average*(10**4)))

print(Average)