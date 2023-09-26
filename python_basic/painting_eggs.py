eggs_size = input()
eggs_color = input()
eggs_batch = int(input())
prise_one_batch = 0

if eggs_size == 'Large':
    if eggs_color == 'Red':
        prise_one_batch = 16
    elif eggs_color == 'Green':
        prise_one_batch = 12
    elif eggs_color == 'Yellow':
        prise_one_batch = 9

if eggs_size == 'Medium':
    if eggs_color == 'Red':
        prise_one_batch = 13
    elif eggs_color == 'Green':
        prise_one_batch = 9
    elif eggs_color == 'Yellow':
        prise_one_batch = 7

if eggs_size == 'Small':
    if eggs_color == 'Red':
        prise_one_batch = 9
    elif eggs_color == 'Green':
        prise_one_batch = 8
    elif eggs_color == 'Yellow':
        prise_one_batch = 5

total_price = eggs_batch * prise_one_batch
final_price = total_price - (total_price * 0.35)

print(f"{final_price :.2f} leva.")





