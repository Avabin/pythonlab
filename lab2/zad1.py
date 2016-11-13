import re

text = "jan@onremove_thiset.pl"
toremove = "remove_this"

x = re.search(toremove, text)
y = text[:x.start()] + text[x.end():]

print(y)
