def validated_password(some_passsword):
    list_of_errors = []
    if len(some_passsword) < 6 or len(some_passsword) > 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not some_passsword.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digit_char = 0
    for char in some_passsword:
        if char.isdigit():
            digit_char += 1
    if digit_char < 2:
        list_of_errors.append("Password must have at least 2 digits")
    if len(list_of_errors) == 0:
        print('Password is valid')
    return list_of_errors



password = input()
print("\n".join(validated_password(password)))