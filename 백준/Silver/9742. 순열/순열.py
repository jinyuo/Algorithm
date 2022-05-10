from itertools import permutations
from math import factorial
while True:
    try:
        inp, l = __import__('sys').stdin.readline().split()
    except:
        exit()
    l = int(l)
    if l > factorial(len(inp)):
        print(inp, l, "= No permutation")
        continue
    i = 0
    for t in permutations(inp, len(inp)):
        i += 1
        if i == l:
            print(inp, l, "=", ''.join(t))