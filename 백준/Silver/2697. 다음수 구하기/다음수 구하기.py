import sys
t = int(sys.stdin.readline())
for _ in range(t):
    a = list(str(sys.stdin.readline()[:-1]))
    a = [i for i in a]
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        print("BIGGEST")
        continue
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    a = a[:i] + a[i:][::-1]
    print("".join(i for i in a))