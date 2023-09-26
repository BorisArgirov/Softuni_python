mussala_climbers = 0
monblan_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

climbers_group_number = int(input())

for _ in range(climbers_group_number):
    current_climbers = int(input())
    if current_climbers < 6:
        mussala_climbers += current_climbers
    elif current_climbers < 13:
        monblan_climbers += current_climbers
    elif current_climbers < 26:
        kilimanjaro_climbers += current_climbers
    elif current_climbers < 41:
        k2_climbers += current_climbers
    elif current_climbers >= 41:
        everest_climbers += current_climbers

total_climbers = mussala_climbers + monblan_climbers + kilimanjaro_climbers + k2_climbers + everest_climbers

mussala_percent = mussala_climbers / total_climbers * 100
monblan_percent = monblan_climbers / total_climbers * 100
kilimanjaro_percent = kilimanjaro_climbers / total_climbers * 100
k2_percent = k2_climbers / total_climbers * 100
everest_percent = everest_climbers / total_climbers * 100

print(f'{mussala_percent :.2f}%')
print(f'{monblan_percent :.2f}%')
print(f'{kilimanjaro_percent :.2f}%')
print(f'{k2_percent :.2f}%')
print(f'{everest_percent :.2f}%')
