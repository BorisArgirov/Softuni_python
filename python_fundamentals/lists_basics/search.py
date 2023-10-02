n = int(input())
word = input()

list = []
filterd_list = []

for _ in range(n):
    strings = input()
    list.append(strings)
    if word in strings:
        filterd_list.append(strings)

print(list)
print(filterd_list)