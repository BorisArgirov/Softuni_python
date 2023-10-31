
def include_coffee(coffee_list, coffee):
    coffee_list.append(coffee)
    return coffee_list

def remove_coffee(coffee_list, position, count):
    if position == "first":
        coffee_list = coffee_list[count:]
    elif position == "last":
        coffee_list = coffee_list[:-count]
    return coffee_list

def prefer_coffee(coffee_list, index1, index2):
    if 0 <= index1 < len(coffee_list) and 0 <= index2 < len(coffee_list):
        coffee_list[index1], coffee_list[index2] = coffee_list[index2], coffee_list[index1]
    return coffee_list


def reverse_coffees(coffee_list):
    coffee_list = coffee_list[::-1]
    return coffee_list

coffees = input().split()
n = int(input())

for _ in range(n):
    command = input().split()
    action = command[0]

    if action == "Include":
        coffee = command[1]
        coffees = include_coffee(coffees, coffee)
    elif action == "Remove":
        position = command[1]
        count = int(command[2])
        coffees = remove_coffee(coffees, position, count)
    elif action == "Prefer":
        index1 = int(command[1])
        index2 = int(command[2])
        coffees = prefer_coffee(coffees, index1, index2)
    elif action == "Reverse":
        coffees = reverse_coffees(coffees)

print("Coffees:")
print(" ".join(coffees))


