target_book = input()
current_command = input()

checked_book_count = 0

while current_command != 'No More Books':
    current_book = current_command
    if current_book == target_book:
        break
    checked_book_count += 1
    current_command = input()

if current_command != 'No More Books':
    print(f'You checked {checked_book_count} books and found it.')
else:
    print("The book you search is not here!")
    print(f'You checked {checked_book_count} books.')



