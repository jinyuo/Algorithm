import sys
m, n = map(int, sys.stdin.readline().split())
intstr = {"0": "zero", "1": 'one', "2": 'two', "3": 'three', "4": 'four', "5": "five", "6": "six", "7": "seven",
          "8": "eight", "9": "nine"}
d = dict()
for i in range(m, n + 1):
    d[i] = " ".join([intstr[stri] for stri in str(i)])
sort = sorted(d, key=lambda x: d[x])
for i in range(1, len(sort) + 1):
    print(sort[i - 1], end=" ")
    if i % 10 == 0:
        print()