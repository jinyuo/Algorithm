import sys
s = [[int(sys.stdin.readline()) for _ in range(10)] for _ in range(2)]
print(sum(sorted(s[0])[7:]), sum(sorted(s[1])[7:]))