string_list = [char for char in input() if char != " "]

letters = {}

for letter in string_list:
    if letter not in letters.keys():
        letters[letter] = 0
    letters[letter] += 1

for key, value in letters.items():
    print(key, '->', value)