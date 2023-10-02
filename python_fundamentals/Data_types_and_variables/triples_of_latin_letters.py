symbols_number = int(input())
for first_number in range(symbols_number):
    for second_number in range(symbols_number):
        for third_number in range(symbols_number):
            print(f'{chr(97 + first_number)}{chr(97 + second_number)}{chr(97 + third_number)}')
