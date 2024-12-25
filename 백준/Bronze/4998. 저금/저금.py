import sys
import math

while True:
    try:
        N, B, M = map(float, sys.stdin.readline().strip().split(' '))
        print(math.ceil(math.log(M / N, (1 + B / 100))))
    except:
        break
   