company_names = {}

while True:
    command = input()

    if command == 'End':
        break

    company_name, employees = command.split('->')


    if company_name not in company_names.keys():
        company_names[company_name] = []
    if employees not in company_names[company_name]:
        company_names[company_name].append(employees)

for company_name, employees in company_names.items():
    print(company_name)
    for employee in employees:
        print(f'--{employee}')