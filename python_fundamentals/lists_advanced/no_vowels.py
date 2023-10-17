text = input()

no_vowels_text = [char for char in text if char.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(no_vowels_text))