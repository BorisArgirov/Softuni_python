def all_characters(one, two):
    list = []
    for char in range(ord(one) + 1, ord(two)):
        list.append(chr(char))
    return list


first_char = input()
second_char = input()
final_result = all_characters(first_char, second_char)
print(" ".join(final_result))