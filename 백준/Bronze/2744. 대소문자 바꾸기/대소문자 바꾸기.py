import sys
s = sys.stdin.readline()
l = ""
for i in range(len(s)):
    if s[i].isupper():
        l += s[i].lower()
    else:
        l += s[i].upper()
print(l)