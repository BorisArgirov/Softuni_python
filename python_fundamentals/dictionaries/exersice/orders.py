products_info = {}

while True:
    command = input()
    if command == 'buy':
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = float(quantity)

    if name not in products_info:
        products_info[name] = {"price": price, "quantity":quantity}
    else:
        products_info[name]['quantity'] += quantity
        products_info[name]['price'] = price

for product, info in products_info.items():
    total_price = info['price'] * info['quantity']
    print(f"{product} -> {total_price:.2f}")
