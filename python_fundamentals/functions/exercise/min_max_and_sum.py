list_of_numbers = input().split()

list_of_numbers = [int(number) for number in list_of_numbers]
print(f"The minimum number is {min(list_of_numbers)}")
print(f"The maximum number is {max(list_of_numbers)}")
print(f"The sum number is: {sum(list_of_numbers)}")