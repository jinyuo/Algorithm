import sys
i = 1
x = int(sys.stdin.readline())
while x > i * (i + 1) // 2:
    i += 1

c = i
p = 1
for _ in range(i * (i - 1) // 2, x - 1):
    c -= 1
    p += 1

if i % 2 == 0:
    c, p = p, c
print(f"{c}/{p}")