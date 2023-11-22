text = input()

final_message = ''
repetitions = ''
current_message = ''

for index in range(len(text)):
    if not text[index].isdigit():
        current_message += text[index].upper()
    else:
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetitions += text[next_symbols]
        final_message += current_message * int(repetitions)
        current_message = ''
        repetitions = ''

print(f'Unique symbols used: {len(set(final_message))}')
print(f'{final_message}')

