import datetime

back = datetime.datetime.now() + datetime.timedelta(days=-5)
forth = datetime.datetime.now() + datetime.timedelta(days=5)
print(datetime.datetime.now())
print(str(forth))
print(str(back))