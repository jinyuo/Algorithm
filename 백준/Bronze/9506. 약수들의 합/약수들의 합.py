import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    f = []
    d = 1
    while d <= n / 2:
        if n % d == 0:
            f.append(d)
        d += 1

    print(f"{n} = " + ' + '.join(str(fs) for fs in f) if sum(f) == n else f"{n} is NOT perfect.")