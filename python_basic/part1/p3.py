import datetime

print(dir(datetime))

time_str = datetime.datetime.now()
print(time_str.strftime("%Y-%m-%d %H:%M:%S"))
