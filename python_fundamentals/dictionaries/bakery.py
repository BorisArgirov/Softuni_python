bakery = {}

command = input().split()

for index in range(0, len(command), 2):
    key = command[index]
    value = int(command[index + 1])
    bakery[key] = value
print(bakery)

