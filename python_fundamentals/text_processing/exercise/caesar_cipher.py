text = input()
the_passwprd = [ord(char) + 3 for char in text]
for char in the_passwprd:
    print(chr(char), end='')



