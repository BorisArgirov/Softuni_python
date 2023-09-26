controla_minutes = int(input())
second_controla = int(input())
lenght_trace = float(input())
second_100_meters = int(input())
controla_total = controla_minutes * 60 + second_controla
reduction = lenght_trace / 120 * 2.5
total_time = lenght_trace / 100 * second_100_meters - reduction

if total_time <= controla_total:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time :.3f}.")
else:
    nedostig = controla_total - total_time
    print(f"No, Marin failed! He was {abs(nedostig) :.3f} second slower.")
