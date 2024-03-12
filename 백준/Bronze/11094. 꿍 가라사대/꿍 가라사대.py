import sys
n = int(sys.stdin.readline())
for _ in range(n):
    s = sys.stdin.readline()[:-1]

    if s.find('Simon says') > -1:
        print(s.replace('Simon says', ''))