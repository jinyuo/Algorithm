import sys
for n in sys.stdin:
    if n == '\n':
        break
    num = 1
    while True:
        if num % int(n) == 0:
            print(len(str(num)))
            break
        num = num * 10 + 1