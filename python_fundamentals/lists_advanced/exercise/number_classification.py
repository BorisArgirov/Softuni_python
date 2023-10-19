numbers = input().split(', ')

int_numbers = [int(number) for number in numbers]

Positive = []
Negative = []
Even = []
Odd = []

for number in int_numbers:
    if number >= 0:
        Positive.append(number)
    elif number < 0:
        Negative.append(number)
    if number % 2 == 0:
        Even.append(number)
    else:
        Odd.append(number)
print(f'Positive: {", ".join(map(str, Positive))}')
print(f'Negative: {", ".join(map(str, Negative))}')
print(f'Even: {", ".join(map(str, Even))}')
print(f'Odd: {", ".join(map(str, Odd))}')

