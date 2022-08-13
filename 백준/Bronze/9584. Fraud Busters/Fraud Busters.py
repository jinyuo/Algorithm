import sys
import re
code = sys.stdin.readline()[:-1]
code = code.replace("*", ".")
k = int(sys.stdin.readline())
matches = []
for _ in range(k):
    c = sys.stdin.readline()[:-1]
    if re.search(code, c):
        matches.append(c)
print(len(matches))
print("\n".join([m for m in matches]))