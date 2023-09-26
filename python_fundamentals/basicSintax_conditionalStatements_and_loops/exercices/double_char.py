string_ = input()

while string_ != 'End':
    if string_ != 'SoftUni':
        new_string = ''
        for char in string_:
            new_string += char * 2
        print(new_string)
    string_ = input()