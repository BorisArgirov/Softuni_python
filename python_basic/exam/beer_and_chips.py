import math

fan_name = input()
budget = float(input())
beer_botles = int(input())
chips_packets = int(input())

beer_botles_price = beer_botles * 1.20
chips_packets_price = math.ceil(beer_botles_price * 0.45 * chips_packets)

total_price = beer_botles_price + chips_packets_price

if budget >= total_price:
    print(f"{fan_name} bought a snack and has {budget - total_price :.2f} leva left.")
else:
    print(f"{fan_name} needs {total_price - budget :.2f} more leva!")