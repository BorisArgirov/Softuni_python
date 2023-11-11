command = int(input())
register_sys = {}

for users in range(command):

    current_command = input().split()

    if current_command[0] == 'register':
        username = current_command[1]
        plate_number = current_command[2]
        if username not in register_sys:
            register_sys[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")

    if current_command[0] == 'unregister':
        if current_command[1] not in register_sys.keys():
            print(f"ERROR: user {current_command[1]} not found")
        else:
            print(f"{current_command[1]} unregistered successfully")
            del register_sys[current_command[1]]

for usernames, plates in register_sys.items():
    print(f"{usernames} => {plates}")

