text = input().split()
symbols = [char.rstrip('.') for char in  text if ':' in char]
for symbol in symbols:
    print(symbol)
