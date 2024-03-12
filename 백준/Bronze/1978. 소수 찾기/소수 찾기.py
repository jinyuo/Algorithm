import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
c = 0
for num in num_list:
    if num == 1:
        continue
    d = 2
    so = False
    while d <= num ** 0.5:
        if num % d == 0:
            so = True
            break
        else:
            d += 2 if d > 2 else 1
    if not so:
        c += 1
print(c)