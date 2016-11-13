import re

email = "Kamil kamil@google.com, Tomek tomek@o2.pl"

regex_email = "\S+@\S+"

x = re.findall(regex_email ,email)

for i in x:
    print(i)
