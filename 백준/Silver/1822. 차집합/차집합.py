import sys
sys.stdin.readline()
a = list(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))
sub = [i for i in sorted(a) if i not in b]
if len(sub) == 0:
    print(0)
else:
    print(len(sub))
    print(*sub)