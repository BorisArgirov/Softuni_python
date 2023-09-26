lenght = int(input())
height = int(input())
width = int(input())
precent_non_empty = float(input())

total_volume = lenght * height * width
total_volume_liters = total_volume / 1000
water_needed = total_volume_liters - (total_volume_liters * (precent_non_empty / 100))
print(water_needed)