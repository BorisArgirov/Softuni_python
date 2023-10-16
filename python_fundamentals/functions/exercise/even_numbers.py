numbers = input().split()
new_list = []
for num in numbers:
    new_list.append(int(num))
is_even = lambda x: x % 2 == 0
result = filter(is_even, new_list)
print(list(result))