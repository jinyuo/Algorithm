import sys
import datetime
b = datetime.datetime.strptime(sys.stdin.readline()[:-1], "%H:%M:%S")
a = datetime.datetime.strptime(sys.stdin.readline()[:-1], "%H:%M:%S")
h, m = divmod((a - b).seconds, 3600)
m, s = divmod(m, 60)
print("24:00:00" if h == m == s == 0 else "{:02}:{:02}:{:02}".format(h, m, s))