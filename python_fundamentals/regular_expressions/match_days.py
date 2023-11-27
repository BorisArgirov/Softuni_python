import re

dates = input()
regex = r'(\d{2})([./-])([A-Z][a-z]{2})\2(\d{4})'

match = re.findall(regex, dates)

for dates in match:
    day = dates[0]
    month = dates[2]
    year = dates[3]

    print(f'Day: {day}, Month: {month}, Year: {year}')