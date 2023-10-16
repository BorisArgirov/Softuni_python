def odd_even_sums(some_number):
    even_num_sum = 0
    odd_num_sum = 0
    for num in some_number:
        num = int(num)
        if num % 2 == 0:
            odd_num_sum += num
        if num % 2 != 0:
            even_num_sum += num
    return odd_num_sum, even_num_sum


single_number = input()
odd_num_sum, even_num_sum = odd_even_sums(single_number)
print(f"Odd sum = {even_num_sum}, Even sum = {odd_num_sum}")
