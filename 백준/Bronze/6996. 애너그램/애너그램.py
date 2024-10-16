import sys
from collections import Counter

t = int(sys.stdin.readline().strip())
for _ in range(t):
    a, b = sys.stdin.readline().split()
    flag = ''
    if sum((Counter(a) | Counter(b)).values()) - sum((Counter(a) & Counter(b)).values()) > 0:
        flag = 'NOT '
    msg = f'{a} & {b} are {flag}anagrams.'
    print(msg)