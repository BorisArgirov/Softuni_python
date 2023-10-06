money_as_string = input().split(', ')
number_of_beggas = int(input())

money_as_intigers = []

for money in money_as_string:
    money_as_intigers.append(int(money))
final_sums = []
start_index = 0
while start_index < number_of_beggas:
    current_begger_sum = 0
    for current_index in range(start_index, len(money_as_intigers), number_of_beggas):
        current_begger_sum += money_as_intigers[current_index]
    final_sums.append(current_begger_sum)
    start_index += 1
print(final_sums)
