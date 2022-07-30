import sys
d, k = map(int, sys.stdin.readline().split())
fib = lambda n: 1 if n <= 2 else fib(n - 1) + fib(n - 2)
x, y = fib(d - 2), fib(d - 1)
for a in range(1, k):
    if (k - (x * a)) % y == 0:
        print(a, (k - x * a) // y, sep='\n')
        exit()