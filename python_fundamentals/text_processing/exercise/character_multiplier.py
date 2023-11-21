first_string, second_string = input().split()
total_sum = 0

for char1, char2 in zip(first_string, second_string):
    total_sum += ord(char1) * ord(char2)

if len(first_string) > len(second_string):
    total_sum += sum(ord(char) for char in first_string[len(second_string):])

elif len(second_string) > len(first_string):
    total_sum += sum(ord(char) for char in second_string[len(first_string):])

print(total_sum)