sweet = input()
sweet_count = int(input())
day_of_month = int(input())
one_cace_price = 0
if sweet == 'Cake':
    if day_of_month <= 15:
        one_cace_price = 24
    elif day_of_month > 15:
        one_cace_price = 28.70
elif sweet == 'Souffle':
    if day_of_month <= 15:
        one_cace_price = 6.66
    elif day_of_month > 15:
        one_cace_price = 9.80
elif sweet == 'Baklava':
    if day_of_month <= 15:
        one_cace_price = 12.60
    elif day_of_month > 15:
        one_cace_price = 16.98

total_price = one_cace_price * sweet_count

if day_of_month <= 22 and 100 < total_price < 200:
    total_price = total_price - (total_price * 0.15)
elif day_of_month <= 22 and total_price > 200:
    total_price = total_price - (total_price * 0.25)
if day_of_month <= 15:
    total_price = total_price - (total_price * 0.10)

print(f'{total_price:.2f}')
