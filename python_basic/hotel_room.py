month = input()
nights = int(input())

studio_night_price = 0
appartment_night_price = 0

if month == 'May' or month == 'October':
    studio_night_price = 50
    appartment_night_price = 65
    if 14 >= nights > 7:
        studio_night_price *= 0.95
    elif nights > 14:
        studio_night_price *= 0.70
elif month == 'June' or month == 'September':
    studio_night_price = 75.20
    appartment_night_price = 68.70
    if nights > 14:
        studio_night_price *= 0.80
elif month == 'July' or month == 'August':
    studio_night_price = 76
    appartment_night_price = 77

if nights > 14:
    appartment_night_price *= 0.90

studio_total_price = nights * studio_night_price
appartment_total_price = nights * appartment_night_price

print(f'Apartment: {appartment_total_price:.2f} lv.')
print(f'Studio: {studio_total_price:.2f} lv.')








