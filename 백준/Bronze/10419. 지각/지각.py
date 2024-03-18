import sys
t = int(sys.stdin.readline())
for _ in range(t):
    print(int(-1 + (1 + 4 * int(sys.stdin.readline())) ** 0.5) // 2)