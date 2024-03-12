import sys
n = int(sys.stdin.readline())
cnt = 0
for b in range(1, 501):
    bp = b ** 2 + n
    a = int(bp ** 0.5)
    if a > 500:
        break
    if bp == a ** 2:
        cnt += 1
print(cnt)