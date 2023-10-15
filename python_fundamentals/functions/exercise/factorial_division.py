def facturial_numbers(number):
    for current_number in range(1, number):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())
first_factorial = facturial_numbers(first_number)
second_factorial = facturial_numbers(second_number)
factorial_result = first_factorial / second_factorial
print(f'{factorial_result:.2f}')
