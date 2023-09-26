command =  input()
prime_sum = 0
unprime_sum = 0

while command != 'stop':
    current_number = int(command)
    is_prime = True
    if current_number < 0:
        print("Number is negative.")
        command = input()
        continue
    is_prime = True

    for num in range(2, current_number):
        if current_number % num == 0:
            is_prime = False
            break

    if is_prime:
        prime_sum += current_number
    else:
        unprime_sum += current_number
    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {unprime_sum}")
