product = input()
quantity = int(input())

def total_price(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "coke":
        return quantity * 1.40
    elif product == "water":
        return quantity * 1.00
    elif product == "snacks":
        return quantity * 2.00

result = total_price(product, quantity)
print(f'{result:.2f}')