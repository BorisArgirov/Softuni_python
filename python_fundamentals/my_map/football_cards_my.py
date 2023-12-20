team_a = ["A-" + str(num) for num in range(1, 12)]
team_b = ["B-" + str(num) for num in range(1, 12)]

players = input().split()

for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        break


if len(team_a) < 7 or len(team_b) < 7:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
    print(f"Game was terminated")
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")