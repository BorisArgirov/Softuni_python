factor = int(input())
count = int(input())
list = []

for number in range(1, count + 1):
    curent_number = number * factor
    list.append(curent_number)
print(list)

