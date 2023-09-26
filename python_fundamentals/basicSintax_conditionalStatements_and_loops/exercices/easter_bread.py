budget = float(input())
price_per_kg_flour = float(input())

price_per_pack_eggs = price_per_kg_flour * 0.75
price_per_liter_milk = price_per_kg_flour * 1.25
price_per_250ml_milk = price_per_liter_milk / 4

loaves = 0
colored_eggs = 0

while budget >= price_per_kg_flour + price_per_pack_eggs + price_per_250ml_milk:
    loaves += 1
    colored_eggs += 3
    budget -= (price_per_kg_flour + price_per_pack_eggs + price_per_250ml_milk)

    if loaves % 3 == 0:
        lost_eggs = loaves - 2
        colored_eggs -= lost_eggs

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
