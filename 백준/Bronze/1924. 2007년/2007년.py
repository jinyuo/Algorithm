import sys
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dow = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
m, d = map(int, sys.stdin.readline().split())
g = sum([days[i] for i in range(m - 1)]) + d - 1
print(dow[g % 7])