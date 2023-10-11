numbers = input().split()

def rounding_list(numbers):
    rounded_num_list = []
    for number in numbers:
        float_number = float(number)
        rounded_num_list.append(round(float_number))
    return rounded_num_list
result = rounding_list(numbers)
print(result)


                                 