food_kilograms = int(input())
food_grams = food_kilograms * 1000
total_eated = 0
command = input()

while command != 'Adopted':
    current_eated = int(command)
    total_eated += current_eated
    command = input()

if food_grams >= total_eated:
    print(f"Food is enough! Leftovers: {food_grams - total_eated} grams." )
else:
    print(f"Food is not enough. You need {total_eated - food_grams} grams more.")
