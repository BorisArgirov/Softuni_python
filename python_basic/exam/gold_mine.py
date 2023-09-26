location_count = int(input())

for location in range(location_count):
    waited_average_yield_day = float(input())
    days_count_location = int(input())
    total_yield = 0
    for days in range(days_count_location):
        day_yield = float(input())
        total_yield += day_yield
    average_day_yield = total_yield / days_count_location

    if average_day_yield >= waited_average_yield_day:
        print(f"Good job! Average gold per day: {average_day_yield :.2f}.")
    else:
        print(f"You need {waited_average_yield_day - average_day_yield :.2f} gold.")

