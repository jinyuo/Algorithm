import sys
while True:
    s = int(sys.stdin.readline())
    if s == 0:
        exit()
    step = [s]
    t = 1
    while s // 10 > 0:
        while s // 10 > 0:
            t *= s % 10
            s //= 10
        t *= s
        step.append(t)
        s = t
        t = 1
    print(" ".join(str(ss) for ss in step))