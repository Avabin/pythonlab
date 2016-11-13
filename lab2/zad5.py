import re

text = "Ala ma kotka, kotek jest Ali"

x = re.sub("[kK]otka", '*', text)
print(x)
