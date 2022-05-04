import sys
i = 1
x = int(sys.stdin.readline())
while x > i * (i + 1) // 2:
    i += 1
if i % 2 == 1:
    c = i
    p = 1

    for _ in range(i * (i - 1) // 2, x - 1):
        c -= 1
        p += 1
else:
    c = 1
    p = i
    for _ in range(i * (i - 1) // 2, x - 1):
        c += 1
        p -= 1
print(f"{c}/{p}")