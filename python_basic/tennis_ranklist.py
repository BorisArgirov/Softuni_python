tournament_count = int(input())
ranglist_points = int(input())

total_points = ranglist_points
wins = 0
tournament_points = 0


for _ in range(tournament_count):
    tournament_result = input()
    if tournament_result == 'W':
        total_points += 2000
        tournament_points += 2000
        wins += 1
    elif tournament_result == 'F':
        total_points += 1200
        tournament_points += 1200
    elif tournament_result == 'SF':
        total_points += 720
        tournament_points += 720

average_points = tournament_points / tournament_count
wins_percent = (wins / tournament_count) * 100

import  math
print(f'Final points: {total_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{wins_percent :.2f}%')

#7 1200 SF F W F W SF W
#4 750 SF W SF W
#5 1400 F SF W W SF

