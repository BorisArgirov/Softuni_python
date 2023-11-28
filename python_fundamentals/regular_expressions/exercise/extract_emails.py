import re

sentence = input()

pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_\,]*)@([a-z\-]+)(\.[a-z]+)+)\b"

match = re.findall(pattern, sentence)

for mail in match:
    print(mail[0])