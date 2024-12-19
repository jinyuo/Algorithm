import math
import sys
from math import log

while True:
    try:
        N, B, M = map(float, sys.stdin.readline().strip().split(' '))
        print(math.ceil(log(M / N, (1 + B / 100))))
    except:
        break
   