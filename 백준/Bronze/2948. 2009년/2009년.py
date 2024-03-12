import sys
import time

d, m = map(int, sys.stdin.readline().split())
wdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
t = time.strptime(f"2009-{m}-{d}", "%Y-%m-%d")
print(wdays[t.tm_wday])