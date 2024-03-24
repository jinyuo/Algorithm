import sys
en = [int(sys.stdin.readline()) for _ in range(5)]
x = en[0] * en[4]
y = en[1] if en[4] <= en[2] else en[1] + en[3] * (en[4] - en[2])
print(min(x, y))