import re

text = "Nie lubię w poniedziałki wcześnie wstawać."
x = re.findall(r"'([N]\w+)", text)
print(x)

y = re.findall(r"\b\w{3}\b", text)
print(y)

z = re.findall(r"\b\w", text)
print(z)
