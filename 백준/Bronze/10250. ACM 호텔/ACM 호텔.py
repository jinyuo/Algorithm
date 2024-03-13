import sys

T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    y, x = divmod(N - 1, H)
    print(f"{x + 1}{y + 1:02d}")