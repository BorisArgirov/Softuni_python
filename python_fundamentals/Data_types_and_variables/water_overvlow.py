number_of_lines = int(input())
water_tank_capacity = 255
current_liters = 0

for number in range(number_of_lines):
    liters_of_water = int(input())

    if water_tank_capacity - liters_of_water < 0:
        print("Insufficient capacity!")
        continue
    current_liters += liters_of_water
    water_tank_capacity -= liters_of_water
print(current_liters)