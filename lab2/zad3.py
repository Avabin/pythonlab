import re

tel = "345-03-02"
tosub = "\-"
x = re.sub(tosub, "", tel)

print(x)
