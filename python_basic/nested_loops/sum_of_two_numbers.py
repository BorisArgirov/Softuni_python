start_number = int(input())
end_number = int(input())
magic_number = int(input())
found_combination = False
combination_count = 0

for start_number in range(start_number, end_number + 1):
    for end_number in range(start_number, end_number + 1):
        combination_count += 1
        if start_number + end_number == magic_number:
            found_combination = True
            break
    if found_combination:
        break
if found_combination:
    print(f"Combination N:{combination_count} ({start_number} + {end_number} = {magic_number})")
else:
    print(f"{combination_count} combinations - neither equals {magic_number}")

