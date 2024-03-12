import sys

sec = []
for i in range(2):
    h, m, s = map(int, sys.stdin.readline().split(":"))
    sec.append(h * 60 * 60 + m * 60 + s)
t = sec[1] - sec[0]
print('{0:02d}'.format(t // 60 // 60 % 24), '{0:02d}'.format(t // 60 % 60), '{0:02d}'.format(t % 60), sep=":")