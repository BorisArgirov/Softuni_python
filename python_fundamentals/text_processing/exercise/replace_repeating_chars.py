text = input()

last_added = ''
final_result = ''

for char in text:
    if char != last_added:
        final_result += char
        last_added = char
print(final_result)
