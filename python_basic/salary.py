open_tabs = int(input())
salary = float(input())

fine = 0

for _ in range(open_tabs):
    current_opend_tab = input()
    if current_opend_tab == "Facebook":
        fine += 150
        if fine >= salary:
            print('You have lost your salary.')
            break
    elif current_opend_tab == "Instagram":
        fine += 100
        if fine >= salary:
            print('You have lost your salary.')
            break
    elif current_opend_tab == 'Reddit':
        fine += 50
        if fine >= salary:
            print('You have lost your salary.')
            break

if salary > fine:
    print(f'{int(salary - fine)}')