import datetime
import time
import calendar

print(datetime.datetime.now())

print(calendar.day_name[datetime.date.today().weekday()], datetime.datetime.today().weekday())
tt = datetime.date.today().timetuple()
print("day of month : ", tt.tm_mday,
      "\nday of year  :", tt.tm_yday)
