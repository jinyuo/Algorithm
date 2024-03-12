import sys
n = int(sys.stdin.readline())
for _ in range(n):
    f, r = sys.stdin.readline().split("-")
    tmp = 0
    for i in range(len(f)):
        tmp += (ord(f[i]) - ord("A")) * pow(26, len(f) - 1 - i)

    print("nice" if abs(tmp - int(r)) <= 100 else "not nice")