days_to_stay = int(input())
type_of_room = input()
rating = input()

room_per_night_price = 18
aparment_per_night_price = 25
president_apartment_night_price = 35
nights_to_stay = days_to_stay - 1
price = 0

if type_of_room == 'room for one person':
    price = nights_to_stay * room_per_night_price
elif type_of_room == 'apartment':
    if days_to_stay < 10:
        price = nights_to_stay * aparment_per_night_price * 0.70
    elif 10 <= days_to_stay <= 15:
        price = nights_to_stay * aparment_per_night_price * 0.65
    else:
        price = nights_to_stay * aparment_per_night_price * 0.50
elif type_of_room == 'president apartment':
    if days_to_stay < 10:
        price = nights_to_stay * president_apartment_night_price * 0.90
    elif 10 <= days_to_stay <= 15:
        price = nights_to_stay * president_apartment_night_price * 0.85
    else:
        price = nights_to_stay * president_apartment_night_price * 0.80

if rating == 'positive':
    price = price + (price * 0.25)
if rating == 'negative':
    price = price - (price * 0.10)

print(f'{price:.2f}')


