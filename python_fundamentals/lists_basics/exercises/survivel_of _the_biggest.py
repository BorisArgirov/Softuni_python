list_of_numbers = input().split()
numbers_to_remove = int(input())
numbers_list = []

for numbers in list_of_numbers:
    numbers_list.append(int(numbers))

for num in range(numbers_to_remove):
    numbers_list.remove(min(numbers_list))
numbers_list = [str(num) for num in numbers_list]
result = ', '.join(numbers_list)
print(result)

