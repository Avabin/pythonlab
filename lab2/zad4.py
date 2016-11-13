import re

tel = "500-800-4623"

x = re.compile("\w+")
y = x.findall(tel)

print(y)
