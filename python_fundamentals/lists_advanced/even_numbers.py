number_list = list(map(int, input().split(', ')))

founded_indices = map(lambda x: x if number_list[x] % 2 == 0 else 'no', range(len(number_list)))
even_indices = list(filter(lambda a: a != 'no', founded_indices))
print(even_indices)
