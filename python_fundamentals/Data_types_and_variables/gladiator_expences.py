lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expences = 0
broken_shield = 0

for lost_fight in range(1, lost_fights_count + 1):

    if lost_fight % 2 == 0:
        total_expences += helmet_price
    if lost_fight % 3 == 0:
        total_expences += sword_price
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        total_expences += shield_price
        broken_shield += 1
        if broken_shield % 2 == 0:
            total_expences += armor_price
print(f"Gladiator expenses: {total_expences:.2f} aureus")