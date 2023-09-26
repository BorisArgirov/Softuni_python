needed_nylon = int(input())
needed_paint = int(input())
needed_thinner = int(input())
work_hours = int(input())

nylon_price_meter = 1.50
total_nylon_price = (needed_nylon + 2) * nylon_price_meter
paint_price_meter = 14.50
total_paint_price = (needed_paint + needed_paint * 0.10) * paint_price_meter
thinner_price_meter = 5.00
total_thinner_price = needed_thinner * thinner_price_meter
bags_price = 0.40

totaal_materials_fee = total_nylon_price + total_paint_price + total_thinner_price + bags_price
work_1_hour = totaal_materials_fee * 0.30
total_work_hours = work_hours * work_1_hour
total_fee = totaal_materials_fee + total_work_hours
print(total_fee)