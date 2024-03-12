import sys
for _ in range(3):
    n = sys.stdin.readline()
    max = 1
    t = 1
    for i in range(7):
        if n[i] == n[i + 1]:
            t += 1
            if i == 6 and max < t:
                max = t
        else:
            if max < t:
                max = t
            t = 1
    print(max)