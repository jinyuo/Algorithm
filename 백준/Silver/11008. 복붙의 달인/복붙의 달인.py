import re
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    s, p = sys.stdin.readline().strip().split()
    cnt_copy = len(re.findall(p, s))
    print(len(s) - len(p) * cnt_copy + cnt_copy)
