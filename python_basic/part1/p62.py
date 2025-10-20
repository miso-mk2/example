days = int(input("日="))
hours = int(input("時="))
minutes = int(input("分="))
seconds = int(input("秒="))

print(f"秒に慣らすと={seconds + minutes*60 + hours*3600 +days*86400}")
