budget = float(input())
kg_flour_price = float(input())

loaves = 0
colored_eggs = 0

eggs_price = kg_flour_price * 0.75
liter_milk_price = kg_flour_price + (kg_flour_price * 0.25)
loave_budget = eggs_price + kg_flour_price + liter_milk_price/4

while budget >= loave_budget:
    loaves += 1
    colored_eggs += 3
    budget -= loave_budget
    if loaves % 3 == 0:
        colored_eggs -= loaves - 2
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")















