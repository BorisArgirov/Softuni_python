def library(input_string):
    shelf = input_string.split('&')
    commands = input().split('|')

    while commands[0] != "Done":
        command = commands[0].strip()

        if command == "Add Book":
            book_name = commands[1].strip()
            if book_name not in shelf:
                shelf.insert(0, book_name)

        elif command == "Take Book":
            book_name = commands[1].strip()
            if book_name in shelf:
                shelf.remove(book_name)

        elif command == "Swap Books":
            book1 = commands[1].strip()
            book2 = commands[2].strip()
            if book1 in shelf and book2 in shelf:
                index1 = shelf.index(book1)
                index2 = shelf.index(book2)
                shelf[index1], shelf[index2] = shelf[index2], shelf[index1]

        elif command == "Insert Book":
            book_name = commands[1].strip()
            if book_name not in shelf:
                shelf.append(book_name)

        elif command == "Check Book":
            index = int(commands[1].strip())
            if 0 <= index < len(shelf):
                print(shelf[index])

        commands = input().split('|')

    print(", ".join(shelf))

shelf_input = input()
library(shelf_input)
