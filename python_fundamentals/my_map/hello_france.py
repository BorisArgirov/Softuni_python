items = input().split('|')
budget = float(input())
clothes_max = 50.00
shoes_max =  35.00
accessories_max = 20.50
price_list = []


for item in items:
    type, price = item.split('->')
    num_price = float(price)
    if type == "Clothes" and num_price < clothes_max and budget >= num_price:
        price_list.append(num_price)
        budget -= num_price
    elif type == "Shoes" and num_price < shoes_max and budget >= num_price:
        price_list.append(num_price)
        budget -= num_price
    elif type == "Accessories" and num_price < accessories_max and budget >= num_price:
        price_list.append(num_price)
        budget -= num_price

new_prices = [((float(prices)) * 0.4 + float(prices)) for prices in price_list]
profit = sum(new_prices) - sum(price_list)
final_budget = budget + sum(new_prices)

for my_price in new_prices:
    print(f"{my_price:.2f}", end=' ')
print(f"\nProfit: {profit:.2f}")

if final_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")





