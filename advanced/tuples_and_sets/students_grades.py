students_number = int(input())


student_record = {}
for _ in range(students_number):
    name, grade = input().split()
    if name not in student_record:
        student_record[name] = []
    student_record[name].append(float(grade))

for names, grades in student_record.items():
    my_grades = " ".join(str(f"{grade:.2f}") for grade in grades)
    print(f"{names} -> {my_grades} (avg: {sum(grades) / len(grades):.2f})")


