eastern_count = int(input())
best_points = 0
best_baker_name = ''
for eastern in range(eastern_count):
    baker_name = input()
    command = input()
    total_points = 0
    while command != 'Stop':
        person_rating_points = int(command)
        total_points += person_rating_points
        command = input()
    print(f"{baker_name} has {total_points} points.")
    if total_points > best_points:
        best_rating = total_points
        best_baker_name = baker_name
        print(f"{baker_name} is the new number 1!")
print(f"{best_baker_name} won competition with {best_points} points!")




