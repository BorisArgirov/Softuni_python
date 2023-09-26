budget = float(input())
season = input()

expence = 0
destination = ''

if  budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        expence = budget * 0.30
        rest_place = 'Camp'
    elif season == 'winter':
        expence = budget * 0.70
        rest_place = 'Hotel'
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        expence = budget * 0.40
        rest_place = 'Camp'
    elif season == 'winter':
        expence = budget * 0.80
        rest_place = 'Hotel'
else:
    destination = 'Europe'
    expence = budget * 0.90
    rest_place = 'Hotel'


print(f'Somewhere in {destination}')
print(f'{rest_place} - {expence:.2f}')