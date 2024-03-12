import sys
n = int(sys.stdin.readline())
c = 0
for _ in range(n):
    word = sys.stdin.readline()[:-1]
    i = 0
    while i < len(word) - 1:
        if word[i:i + 2] == word[i] * 2:
            word = word[:i] + word[i + 1:]
        else:
            i += 1
    if len(word) == len(set(word)):
        c += 1
print(c)