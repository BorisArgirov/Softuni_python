orders_number = int(input())
total_price = 0

for order in range(orders_number):
    capsule_price = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if 0.01 <= capsule_price <= 100 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        one_order_price = capsule_price * days * capsules_needed_per_day
        print(f"The price for the coffee is: ${one_order_price:.2f}")
        total_price += one_order_price
    else:
        continue
print(f"Total: ${total_price:.2f}")



