events = input().split('|')
energy = 100
coins = 100
not_events = False

for event in events:
    current_event = event.split('-')
    if current_event[0] == "rest":
        current_energy = energy
        energy += int(current_event[1])
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif current_event[0] == "order":
        if energy >= 30:
            coins += int(current_event[1])
            energy -= 30
            print(f"You earned {current_event[1]} coins.")
        else:
            print("You had to rest!")
            energy += 50
    else:
        if coins >= int(current_event[1]):
            coins -= int(current_event[1])
            print(f"You bought {current_event[0]}.")

        else:
            print(f"Closed! Cannot afford {current_event[0]}.")
            not_events = True
            break

if not_events == False:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")









