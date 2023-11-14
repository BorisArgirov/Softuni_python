list_of_char = input().split(', ')

char_dictionary = {chr:ord(chr) for chr in list_of_char}

print(char_dictionary)