import sys
t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(f"Scenario #{i + 1}:", (m * (m + 1) - n * (n - 1)) // 2, "", sep="\n")