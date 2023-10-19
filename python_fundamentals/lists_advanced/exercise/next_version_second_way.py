version = input()
new_version = version.replace(".", "")
next_version = int(new_version) + 1
print('.'.join(str(next_version)))