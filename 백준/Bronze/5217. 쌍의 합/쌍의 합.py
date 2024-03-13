import sys
n = int(sys.stdin.readline())
for _ in range(n):
    c = int(sys.stdin.readline())
    l = [(i, c - i) for i in range(1, c // 2 + 1) if i != c - i]
    print(f"Pairs for {c}:", ", ".join(f"{x} {y}" for x, y in l))