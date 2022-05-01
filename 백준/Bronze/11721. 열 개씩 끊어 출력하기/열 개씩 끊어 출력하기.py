import sys
s = sys.stdin.readline()
while s:
    print(s[:10 if len(s) // 10 > 0 else len(s) % 10])
    s = s[10:]