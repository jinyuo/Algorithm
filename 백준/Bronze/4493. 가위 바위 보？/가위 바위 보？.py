import sys
t = int(sys.stdin.readline())
for _ in range(t):
    w = [0] * 2
    n = int(sys.stdin.readline())
    for _ in range(n):
        p1, p2 = sys.stdin.readline().split()
        if p1 != p2:
            w[1 if (p1 == "R" and p2 == "P") or (p1 == "P" and p2 == "S") or (p1 == "S" and p2 == "R") else 0] += 1

    print("TIE" if w[0] == w[1] else f"Player {1 if w[0] > w[1] else 2}")