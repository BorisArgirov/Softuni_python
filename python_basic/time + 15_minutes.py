hour = int(input())
minute = int(input())

if hour >= 24:
    print('wrong input hours')
elif minute >= 60:
    print('wrong input minutes')
else:
    minute += 15
    hour += minute // 60
    minute %= 60
    hour %= 24

print(f"{hour:2d}:{minute:02d}")
