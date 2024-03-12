import sys
t = int(sys.stdin.readline())
for _ in range(t):
    i = sys.stdin.readline()
    s = str(int(i) + int(i[::-1]))
    print("YES" if s == s[::-1] else "NO")