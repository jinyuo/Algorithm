import sys
m, n = map(int, sys.stdin.readline().split())
intstr = ["zero", 'one', 'two', 'three', 'four', "five", "six", "seven", "eight", "nine"]
d = dict()
for i in range(m, n + 1):
    d[i] = " ".join([intstr[int(stri)] for stri in str(i)])
sort = sorted(d, key=lambda x: d[x])
for i in range(1, len(sort) + 1):
    print(sort[i - 1], end=" ")
    if i % 10 == 0:
        print()