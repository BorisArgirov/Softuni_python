seconds_first = int(input())
seconds_second = int(input())
seconds_third = int(input())

sum_seconds = seconds_first + seconds_second + seconds_third

sum_seconds_as_minutes = sum_seconds // 60
sum_seconds_as_seconds = sum_seconds % 60

print(f'{sum_seconds_as_minutes}:{sum_seconds_as_seconds :02d}')