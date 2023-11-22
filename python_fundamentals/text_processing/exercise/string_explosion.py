string = input()
final_string = ''
streng = 0

for index in range(len(string)):

    if streng > 0 and string[index] != '>':
        streng -= 1

    elif string[index] == '>':
        streng += int(string[index + 1])
        final_string += string[index]

    else:
        final_string += string[index]

print(final_string)

