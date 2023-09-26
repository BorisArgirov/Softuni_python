pages_totaal = int(input())
pages_per_hour = int(input())
days = int(input())
total_hours = pages_totaal // pages_per_hour
hours_needed_per_day = total_hours / days

print(hours_needed_per_day)