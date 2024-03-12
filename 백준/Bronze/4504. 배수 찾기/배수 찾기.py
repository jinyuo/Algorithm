import sys
n = int(sys.stdin.readline())
while True:
    l = int(sys.stdin.readline())
    if l == 0:
        exit()
    print(f"{l} is a multiple of {n}." if l % n == 0 else f"{l} is NOT a multiple of {n}.")