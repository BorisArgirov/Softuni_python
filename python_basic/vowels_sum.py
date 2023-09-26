text = input()
char_sum = 0

for char in text:
    if char == 'a':
        char_sum += 1
    elif char == 'e':
        char_sum += 2
    elif char == 'i':
        char_sum += 3
    elif char == 'o':
        char_sum += 4
    elif char == 'u':
        char_sum += 5
print(char_sum)
