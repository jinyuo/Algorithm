import operator
import sys
from itertools import accumulate

def check(N):
    if len(N) != 1:
        for i in range(1, len(N)):
            a = list(accumulate([int(i) for i in N[:i]], operator.mul))[-1]
            b = list(accumulate([int(i) for i in N[i:]], operator.mul))[-1]
            if a == b:
                return True
    return False

N = sys.stdin.readline().strip()
print('YES' if check(N) else 'NO')