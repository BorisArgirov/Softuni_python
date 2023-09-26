"""hours_of_day = int(input())
day_of_week = input()

if day_of_week == 'Monday':
    if hours_of_day >= 10 and hours_of_day <= 18:
        print('open')
    else:
        print('closed')
elif day_of_week == 'Tuesday':
    if 10 <= hours_of_day <= 18:
        print('open')
    else:
        print('closed')
elif day_of_week == 'Wednesday':
    if 10 <= hours_of_day <= 18:
        print('open')
    else:
        print('closed')
elif day_of_week == 'Thursday':
    if 10 <= hours_of_day <= 18:
        print('open')
    else:
        print('closed')
elif day_of_week == 'Friday':
    if 10 <= hours_of_day <= 18:
        print('open')
    else:
        print('closed')
elif day_of_week == 'Saturday':
    if 10 <= hours_of_day <= 18:
        print('open')
    else:
        print('closed')
elif day_of_week == 'Sunday':
    print('closed')"""

hours_of_day = int(input())
day_of_week = input()
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',]
opening_time = 10 <= hours_of_day <= 18

if day_of_week in week_days and opening_time == True:
    print('open')
else:
    print('closed')







