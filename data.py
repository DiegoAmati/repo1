import datetime

x = datetime.datetime.now()
y = datetime.datetime(2006, 8, 21)


print(x.strftime("%A" " " "%d"  " " "%B" " "  "%Y"))
print(y.strftime("%A" " " "%d"  " " "%B" " "  "%Y"))

d= datetime.timedelta(x - y)
print(d.strftime("%A" " " "%d"  " " "%B" " "  "%Y"))