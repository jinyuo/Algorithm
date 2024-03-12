import sys
t = int(sys.stdin.readline())
gs = [1, 2, 3, 3, 4, 10]
ss = [1, 2, 2, 2, 3, 5, 10]
for i in range(1, t + 1):
    g = list(map(int, sys.stdin.readline().split()))
    s = list(map(int, sys.stdin.readline().split()))
    g = [g[j] * gs[j] for j in range(len(g))]
    s = [s[j] * ss[j] for j in range(len(s))]
    if sum(g) > sum(s):
        print(f"Battle {i}: Good triumphs over Evil")
    elif sum(g) < sum(s):
        print(f"Battle {i}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {i}: No victor on this battle field")