vacation_price = float(input())
puzzle_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
talking_dolls_price = 3
teddy_bears_price = 4.10
minions_price = 8.20
trucks_price = 2


total_toys_price = (puzzle_count * puzzle_price) + (talking_dolls_count * talking_dolls_price)\
    + (teddy_bears_count * teddy_bears_price) + (minions_count * minions_price)\
    + (trucks_count * trucks_price)

total_toys_count = puzzle_count + talking_dolls_count + teddy_bears_count\
    + minions_count + trucks_count

discount = total_toys_price * 0.25
if total_toys_count < 50:
    discount = 0


end_price = total_toys_price - discount
rent = end_price * 0.10
win = end_price - rent
rest1 = win - vacation_price
rest2 = vacation_price - win

if win >= vacation_price:
    print(f'Yes! {rest1:.2f} lv left.')
else:
    print(f'Not enough money! {rest2:.2f} lv needed.')