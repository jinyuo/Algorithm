import sys
t_old = float(sys.stdin.readline())
while True:
    t = float(sys.stdin.readline())
    if t == float(999):
        exit()
    
    print("{0:.2f}".format(t - t_old))
    t_old = t