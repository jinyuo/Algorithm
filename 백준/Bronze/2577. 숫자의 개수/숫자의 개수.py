import sys
m = 1
for _ in range(3):
    m *= int(sys.stdin.readline())
for i in range(10):
    print(str(m).count(str(i)))