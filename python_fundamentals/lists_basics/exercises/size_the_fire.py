fires_with_cells = input().split('#')
amount_of_water = int(input())

effort = 0
total_fire = []

for fire in fires_with_cells:
    curent_fire = fire.split(' = ')
    fire_type = curent_fire[0]
    fire_level_number = int(curent_fire[1])

    if fire_type == 'High' and amount_of_water >= fire_level_number and 81 <= fire_level_number <= 125:
        effort += fire_level_number * 0.25
        amount_of_water -= fire_level_number
        total_fire.append(int(fire_level_number))
    elif fire_type == 'Medium' and amount_of_water >= fire_level_number and 51 <= fire_level_number <= 80:
        effort += fire_level_number * 0.25
        amount_of_water -= fire_level_number
        total_fire.append(int(fire_level_number))
    if fire_type == 'Low' and amount_of_water >= fire_level_number and 1 <= fire_level_number <= 50:
        effort += fire_level_number * 0.25
        amount_of_water -= fire_level_number
        total_fire.append(int(fire_level_number))

print('Cells:')
for i in range(len(total_fire)):
    print(f' - {total_fire[i]}')
print(f'Effort: {effort:.2f}')
print(f"Total Fire: {sum(total_fire)}")