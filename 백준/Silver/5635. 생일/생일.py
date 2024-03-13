import sys
import datetime
n = int(sys.stdin.readline())
d = dict()
for i in range(n):
    name, dd, mm, yy = sys.stdin.readline().split()
    d[datetime.date(int(yy), int(mm), int(dd))] = name
print(d[max(d.keys())], d[min(d.keys())], sep="\n")