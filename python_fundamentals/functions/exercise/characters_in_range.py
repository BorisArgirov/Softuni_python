def all_characters(first_char: str, second_char: str):
    char_list = []
    for character_digit in range(ord(first_char) + 1, ord(second_char)):
        char_list.append(chr(character_digit))
    return char_list


first_character = input()
second_character = input()
total_char = all_characters(first_character, second_character)
print(" ".join(total_char))