result = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break
    my_command = command.split('-')
    username = my_command[0]
    language = my_command[1]

    if language == "banned":
        if username in result:
            del result[username]

    else:
        if len(my_command) > 2:
            points = int(my_command[2])

            if username not in result:
                result[username] = points
            else:
                if result[username] < points:
                    result[username] = points


            if language not in submissions:
                submissions[language] = 1
            else:
                submissions[language] += 1

print("Results:")
for username, points in result.items():
    print(f"{username} | {points}")
print(f"Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")







