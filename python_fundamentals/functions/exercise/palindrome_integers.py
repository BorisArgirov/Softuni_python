def palindrome_integers(some_number):
    if some_number == some_number[::-1]:
        return True
    return False


numbers_list = input().split(', ')
for number_ in numbers_list:
    print(palindrome_integers(number_))