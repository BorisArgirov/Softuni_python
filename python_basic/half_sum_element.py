import sys

input_number = int(input())

max_number = -sys.maxsize
sum_number = 0

for _ in range(input_number):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number

    sum_number += current_number

rest_sum = sum_number - max_number
if max_number == rest_sum:
    print(f'Yes\nSum = {max_number}')
else:
    diff = abs(max_number - rest_sum)
    print(f'No\nDiff = {diff}')




