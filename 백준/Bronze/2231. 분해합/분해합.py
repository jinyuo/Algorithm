import sys

N = int(sys.stdin.readline())
list_constructor = [i for i in range(N - 9 * len(str(N)), N) if i > 0 and i + sum(map(int, str(i))) == N]
print(min(list_constructor) if list_constructor else 0)