import sys
while True:
    a, b, c, d = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        exit()
    age = [abs(c - a), abs(c - b), abs(d - a), abs(d - b)]
    print(min(age), max(age))