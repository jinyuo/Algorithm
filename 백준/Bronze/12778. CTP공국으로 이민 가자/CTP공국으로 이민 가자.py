from string import ascii_uppercase
import sys

t = int(sys.stdin.readline())
for i in range(t):
    type = sys.stdin.readline().split()
    quest = sys.stdin.readline().split()

    if type[1] == 'C':
        result = [str(ascii_uppercase.index(q) + 1) for q in quest]
    else:
        result = [ascii_uppercase[int(q) - 1] for q in quest]
    print(" ".join(result))