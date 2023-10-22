days_of_the_plunder = int(input())
one_day_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0

for day in range (1, days_of_the_plunder + 1):
    total_plunder += one_day_plunder
    if day % 3 == 0:
        total_plunder += one_day_plunder * 0.50
    if day % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    collected_percentage = (total_plunder / expected_plunder) * 100
    print(f"Collected only {collected_percentage:.2f}% of the plunder.")
