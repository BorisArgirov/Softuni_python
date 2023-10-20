first_list = input().split(', ')
second_list = input().split(', ')
result_list = []
for word in first_list:
    for words in second_list:
        if word in words:
            result_list.append(word)
            break
print(result_list)

