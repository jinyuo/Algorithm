import sys
import datetime

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
at = datetime.datetime.strptime(f"{a[3]}:{a[4]}:{a[5]}", "%H:%M:%S") - datetime.datetime.strptime(
    f"{a[0]}:{a[1]}:{a[2]}", "%H:%M:%S")
bt = datetime.datetime.strptime(f"{b[3]}:{b[4]}:{b[5]}", "%H:%M:%S") - datetime.datetime.strptime(
    f"{b[0]}:{b[1]}:{b[2]}", "%H:%M:%S")
ct = datetime.datetime.strptime(f"{c[3]}:{c[4]}:{c[5]}", "%H:%M:%S") - datetime.datetime.strptime(
    f"{c[0]}:{c[1]}:{c[2]}", "%H:%M:%S")
print(at.seconds // 3600, at.seconds // 60 % 60, at.seconds % 60)
print(bt.seconds // 3600, bt.seconds // 60 % 60, bt.seconds % 60)
print(ct.seconds // 3600, ct.seconds // 60 % 60, ct.seconds % 60)

