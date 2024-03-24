import sys
from string import ascii_lowercase

r = 31
M = 1234567891
L = int(sys.stdin.readline())
list_a = [ascii_lowercase.index(s) + 1 for s in sys.stdin.readline().strip()]
list_a = [a * (r ** i) % M for i, a in enumerate(list_a)]
print(sum(list_a))