coffie_counter = 0
command = input()

while command != 'END':
    if command.lower() == 'coding' \
            or command.lower() == 'dog' \
            or command.lower() == 'cat' \
            or command.lower() == 'movie':
        if command.islower():
            coffie_counter += 1
        else:
            coffie_counter += 2
    command = input()

if coffie_counter > 5:
    print("You need extra sleep")
else:
    print(coffie_counter)