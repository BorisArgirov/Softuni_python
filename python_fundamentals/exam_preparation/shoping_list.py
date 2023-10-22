initial_list = input().split('!')

while True:
    command = input()

    if command == "Go Shopping!":
        break

    comman_parts = command.split()
    action = comman_parts[0]
    item = comman_parts[1]

    if action == "Urgent":
        if item not in initial_list:
            initial_list.insert(0, item)

    elif action == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)

    elif action == "Correct":
        old_item = item
        new_item = comman_parts[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list[index] = new_item

    elif action == "Rearrange":
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

print(', '.join(initial_list))
