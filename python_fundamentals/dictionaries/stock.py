bakery = {}

command = input().split()

for index in range(0, len(command), 2):
    key = command[index]
    value = int(command[index + 1])
    bakery[key] = value

searched_product = input().split()

for product in searched_product:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")