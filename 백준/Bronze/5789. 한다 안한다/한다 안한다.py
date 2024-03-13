import sys
n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline()[:-1]
    m = len(s) // 2
    print("Do-it" if s[m - 1] == s[m] else "Do-it-Not")