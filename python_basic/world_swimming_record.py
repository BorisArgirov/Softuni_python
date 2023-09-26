record = float(input())
meter_distance = float(input())
seconds_per_meter = float(input())

import math

slowdown_time = math.floor(meter_distance / 15) * 12.5

ivan_distance_time = meter_distance * seconds_per_meter
total_time_ivan = ivan_distance_time + slowdown_time
rest = total_time_ivan - record

if total_time_ivan < record:
    print(f" Yes, he succeeded! The new world record is {total_time_ivan:.2f} seconds.")

if total_time_ivan >= record:
    print(f"No, he failed! He was {rest:.2f} seconds slower.")

