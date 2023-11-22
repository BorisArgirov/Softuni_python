input_strings = input().split()

total_sum = 0

for input_string in input_strings:
    number = int(input_string[1:-1])
    letter_before = input_string[0]
    letter_after = input_string[-1]
    current_sum = 0

    if letter_before.isupper():
        current_sum = number / (ord(letter_before) - 64)
    elif letter_before.islower():
        current_sum = number * (ord(letter_before) - 96)

    if letter_after.isupper():
        current_sum -= ord(letter_after) - 64
    elif letter_after.islower():
        current_sum += ord(letter_after) - 96

    total_sum += current_sum

print(f"{total_sum:.2f}")