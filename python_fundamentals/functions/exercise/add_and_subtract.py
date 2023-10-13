def sum_numbers(first, second):
    return first + second

def subtract(result, third):
    return result - third

def add_and_subtract(first, second, third):
    returned_result = sum_numbers(first, second)
    total_result = subtract(returned_result, third)
    return total_result


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))