import sys
t = int(sys.stdin.readline())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(t):
    s = sys.stdin.readline()[:-1]
    ss = 0
    for a in alphabet:
        if a not in s:
            ss += ord(a)
    print(ss)