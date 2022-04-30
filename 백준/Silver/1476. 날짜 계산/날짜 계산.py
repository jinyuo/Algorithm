import sys
e, s, m = map(int, sys.stdin.readline().split())

i = 0
while True:
    y = 28 * i + s
    if (y % 15 == e or (y % 15 == 0 and e == 15)) and (y % 19 == m or (y % 19 == 0 and m == 19)):
        print(y)
        exit()
    i += 1