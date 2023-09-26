vacation_cost = float(input())
starting_money = float(input())

total_money = starting_money
total_days = 0
spend_days = 0

while True:
    action = input()
    current_money = float(input())
    total_days += 1

    if action == 'spend':
        spend_days += 1
        total_money -= current_money
        if total_money <= 0:
            total_money = 0
        if spend_days >= 5:
            break

    elif action == 'save':
        spend_days = 0
        total_money += current_money
        if total_money >= vacation_cost:
            break

if total_money >= vacation_cost:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(total_days)
