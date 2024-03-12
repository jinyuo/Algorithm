import sys
t = int(sys.stdin.readline())
for _ in range(t):
    c = int(sys.stdin.readline())
    coin_v = [25, 10, 5, 1]
    coin_c = []
    for i in range(4):
        coin_c.append(c // coin_v[i])
        c %= coin_v[i]
    print(" ".join([str(x) for x in coin_c]))