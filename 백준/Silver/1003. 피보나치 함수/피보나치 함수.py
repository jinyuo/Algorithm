import sys
def fibonacci(n):
    if n in d:
        return d[n]

    t1 = fibonacci(n - 1)
    t2 = fibonacci(n - 2)
    d[n] = [t1[i] + t2[i] for i in range(2)]
    return d[n]


t = int(sys.stdin.readline())
d = {0: [1, 0], 1: [0, 1]}
for _ in range(t):
    n = int(sys.stdin.readline())
    fibonacci(n)
    print(d[n][0], d[n][1])
