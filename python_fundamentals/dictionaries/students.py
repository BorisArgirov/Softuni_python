students_info = []
search_course = ''

while True:
    command = input()

    if ':'not in command:
        search_course = command
        break

    name, id, course = command.split(':')

    students_info.append({'name':name, 'ID':id, 'course':course})

for student in students_info:
    if search_course.startswith(student['course'][0:3]):
        print(f'{student["name"]} - {student["ID"]}')






