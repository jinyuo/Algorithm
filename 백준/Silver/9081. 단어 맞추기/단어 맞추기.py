import sys
t = int(sys.stdin.readline())
for _ in range(t):
    word = list(sys.stdin.readline()[:-1])
    i = len(word) - 1
    while i > 0 and word[i - 1] >= word[i]:
        i -= 1
    if i <= 0:
        print("".join(word))
        continue
    j = len(word) - 1
    while word[j] <= word[i - 1]:
        j -= 1
    word[i - 1], word[j] = word[j], word[i - 1]
    j = len(word) - 1
    while i < j:
        word[i], word[j] = word[j], word[i]
        i += 1
        j -= 1
    print("".join(word))
