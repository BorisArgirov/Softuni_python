width = int(input())
lenght = int(input())

cace_pices_total = width * lenght
cace_pieces_left = cace_pices_total

while cace_pices_total > 0:
    command = input()
    if command == 'STOP':
        break
    current_pieces = int(command)
    cace_pieces_left -= current_pieces
    if cace_pieces_left <= 0:
        break

if cace_pieces_left > 0:
    print(f'{cace_pieces_left} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cace_pieces_left)} pieces more.')


