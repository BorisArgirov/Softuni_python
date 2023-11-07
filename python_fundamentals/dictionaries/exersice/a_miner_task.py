recources = {}

while True:

    current_resource = input()
    if current_resource == 'stop':
        break

    quantity = int(input())

    if current_resource not in recources:
        recources[current_resource] = 0
    recources[current_resource] += quantity

for recource, value in recources.items():
    print(f'{recource} -> {value}')

