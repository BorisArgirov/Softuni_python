cats_count = int(input())
#price_food_kg = 12.45
#price_food_gr =  price_food_kg / 1000
group_1 = 0
group_2 = 0
group_3 = 0
total_eated_food = 0

for cats in range(cats_count):
    eated_food = float(input())
    if 100 <= eated_food < 200:
        group_1 += 1
        total_eated_food += eated_food
    elif 200 <= eated_food < 300:
        group_2 += 1
        total_eated_food += eated_food
    elif 300 <= eated_food < 400:
        group_3 += 1
        total_eated_food += eated_food

final_eated_food = total_eated_food / 1000 * 12.45

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {final_eated_food :.2f} lv.")


