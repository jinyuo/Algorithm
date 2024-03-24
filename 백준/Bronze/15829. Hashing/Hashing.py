import sys
from string import ascii_lowercase

r = 31
M = 1234567891
L = int(sys.stdin.readline())
list_a = sys.stdin.readline().strip()

H = 0
for i, a in enumerate(list_a):
    H += (ascii_lowercase.index(a) + 1) * (r ** i) % M
print(H % M)