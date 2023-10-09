number_list = input().split()
list_number = []

for number in number_list:
    list_number.append(abs(float(number)))
print(list_number)
