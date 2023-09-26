serial_name = str(input())
epizode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 1/8
leisure_time = break_duration * 1/4

total_break_time = break_duration - lunch_time - leisure_time
rest_time1 = total_break_time - epizode_duration
rest_time2 = epizode_duration - total_break_time

import math

if total_break_time >= epizode_duration:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(rest_time1)} minutes free time.")
elif total_break_time < epizode_duration:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(rest_time2)} more minutes.")