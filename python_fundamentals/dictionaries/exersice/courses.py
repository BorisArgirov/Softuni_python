courses_dic = {}

while True:
    command = input()
    if command == "end":
        break

    course_name, student_name = command.split(' : ')

    if course_name not in courses_dic:
        courses_dic[course_name] = []
    #if student_name not in courses_dic[course_name]:
    courses_dic[course_name].append(student_name)

for course_name, students in courses_dic.items():
    print(f"{course_name}: {len(students)}")
    for student in students:
        print(f"-- {student}")