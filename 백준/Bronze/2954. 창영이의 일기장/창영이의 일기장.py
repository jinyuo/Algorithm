import sys
s = sys.stdin.readline()[:-1]
vowel = 'aeiou'
i = 0
while i < len(s):
    if s[i] in vowel:
        s = s[:i] + s[i+2:]
    i += 1
print(s)