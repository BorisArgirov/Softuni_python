import sys

count_of_numbers = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for numbers in range(count_of_numbers):
    curent_number = int(input())
    if curent_number > max_number:
        max_number = curent_number
    if curent_number < min_number:
        min_number = curent_number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')