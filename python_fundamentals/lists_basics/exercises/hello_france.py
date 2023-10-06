collection_of_items = input().split('|')
budget = float(input())
ticket_to_france = 150
clothes_price = 50
shoes_price = 35
accessories_price = 20.50
new_prices_list = []
profit = 0

for item in collection_of_items:
    current_item = item.split('->')
    item_type = current_item[0]
    item_value = float(current_item[1])

    if item_type == 'Clothes' and item_value <= clothes_price:
        if budget >= item_value:
            budget -= item_value
            profit += item_value * 0.40
            new_prices_list.append(f'{item_value * 1.40:.2f}')
    elif item_type == 'Shoes' and item_value <= shoes_price:
        if budget >= item_value:
            budget -= item_value
            profit += item_value * 0.40
            new_prices_list.append(f'{item_value * 1.40:.2f}')
    elif item_type == 'Accessories' and item_value <= accessories_price:
        if budget >= item_value:
            budget -= item_value
            profit += item_value * 0.40
            new_prices_list.append(f'{item_value * 1.40:.2f}')

# Calculate the total budget, including the unspent portion
total_budget = budget + sum(float(price) for price in new_prices_list)

print(" ".join(new_prices_list))
print(f"Profit: {profit:.2f}")

if total_budget >= ticket_to_france:
    print("Hello, France!")
else:
    print("Not enough money.")






