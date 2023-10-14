numbers = input().split()

newlist = [int(num) for num in numbers if int(num) % 2 == 0]
print(newlist)