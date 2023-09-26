n = int(input())

for number in range(1, n + 1):
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)
    is_special = False
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True
    print(f'{number} -> {is_special}')



