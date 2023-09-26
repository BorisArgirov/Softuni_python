count_of_numbers = int(input())

left_sum = 0
rigt_sum = 0

for numbers in range(count_of_numbers * 2):
    curent_number = int(input())
    if numbers < count_of_numbers:
        left_sum += curent_number
    else:
        rigt_sum += curent_number

if rigt_sum == left_sum:
    print(f'Yes, sum = {left_sum}')
else:
    difference = abs(rigt_sum - left_sum)
    print(f'No, diff = {difference}')