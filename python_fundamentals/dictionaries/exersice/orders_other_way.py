products_info = {}

while True:
    command = input()
    if command == 'buy':
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = float(quantity)
    total_price = price * quantity

    if name not in products_info:
        products_info[name] = [quantity, price]
    else:
        products_info[name][0] += quantity
        if products_info[name][1] != price:
            products_info[name][1] = price

for product, info in products_info.items():
    total_price = info[1] * info[0]
    print(f"{product} -> {total_price:.2f}")
