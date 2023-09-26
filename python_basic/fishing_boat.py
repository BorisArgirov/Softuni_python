budget = int(input())
season = input()
fishermen_number = int(input())

price = 0
discount = 0
extra_discount = 0

if season == 'Spring':
    price = 3000
    if fishermen_number <= 6:
        discount = 0.10
    elif fishermen_number <= 11:
        discount = 0.15
    else:
        discount = 0.25
    if fishermen_number % 2 == 0:
        extra_discount = 0.05

elif season == 'Summer':
    price = 4200
    if fishermen_number <= 6:
        discount = 0.10
    elif fishermen_number <= 11:
        discount = 0.15
    else:
        discount = 0.25
    if fishermen_number % 2 == 0:
        extra_discount = 0.05

elif season == 'Autumn':
    price = 4200
    if fishermen_number <= 6:
        discount = 0.10
    elif fishermen_number <= 11:
        discount = 0.15
    else:
        discount = 0.25

elif season == 'Winter':
    price = 2600
    if fishermen_number <= 6:
        discount = 0.10
    elif fishermen_number <= 11:
        discount = 0.15
    else:
        discount = 0.25
    if fishermen_number % 2 == 0:
        extra_discount = 0.05

final_price = price * (1 - discount) * (1 - extra_discount)

if budget >= final_price:
    print(f'Yes! You have {budget - final_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {final_price - budget:.2f} leva.')