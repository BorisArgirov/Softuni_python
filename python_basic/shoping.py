budget_petar = float(input())
videocards_number = int(input())
processors_number = int(input())
ram_number = int(input())

price_per_videocard = 250
price_videocards = videocards_number * price_per_videocard
price_processors = processors_number * (price_videocards * 0.35)
price_ram = ram_number * (price_videocards * 0.10)

total_material_sum = price_videocards + price_processors + price_ram

if videocards_number > processors_number:
    total_material_sum = total_material_sum - (total_material_sum * 0.15)

rest1 = budget_petar -  total_material_sum
rest2 = total_material_sum - budget_petar

if budget_petar >= total_material_sum:
    print(f"You have {rest1:.2f} leva left!")

if budget_petar < total_material_sum:
    print(f"Not enough money! You need {rest2:.2f} leva more!")