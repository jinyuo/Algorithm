input = __import__('sys').stdin.readline
from itertools import permutations
from math import factorial

while 1:
    try: a, n = input().split()
    except: break
    n = int(n)
    if n > factorial(len(a)):
        print(a, n, "= No permutation")
        continue
    Z = n
    for Q in permutations(a, len(a)):
        Z-= 1
        if Z == 0: print(a, n, '=', ''.join(Q)); break