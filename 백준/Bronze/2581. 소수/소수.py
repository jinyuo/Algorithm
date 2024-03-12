import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
min = n
sum = 0
for i in range(m, n + 1):
    if i == 1:
        continue
    d = 2
    so = False
    while d <= i ** 0.5:
        if i % d == 0:
            so = True
            break
        else:
            d += 2 if d > 2 else 1
    if not so:
        sum += i
        if i < min:
            min = i

print(sum, min, sep="\n") if sum else print(-1)