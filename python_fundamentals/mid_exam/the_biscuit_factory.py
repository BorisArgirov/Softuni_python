import math

biscuits_number_1worker_per_day = int(input())
num_workers = int(input())
compeating_factory_biscuits_30_days = int(input())
total_production = 0
current_day = 0

for day in range(1, 31):
    if day % 3 == 0:
        daily_production = math.floor(num_workers * biscuits_number_1worker_per_day * 0.75)
    else:
        daily_production = num_workers * biscuits_number_1worker_per_day

    total_production += daily_production

percentage_difference = ((total_production - compeating_factory_biscuits_30_days) / compeating_factory_biscuits_30_days) * 100

print(f"You have produced {round(total_production)} biscuits for the past month.")

if total_production > compeating_factory_biscuits_30_days:
    print(f"You produce {percentage_difference:.2f} percent more biscuits.")
else:
    print(f"You produce {abs(percentage_difference):.2f} percent less biscuits.")




