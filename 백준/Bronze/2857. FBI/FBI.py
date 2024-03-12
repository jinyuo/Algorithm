import sys
l = [i for i in range(1, 6) if sys.stdin.readline().find("FBI") >= 0]
print(" ".join(str(i) for i in l) if len(l) > 0 else "HE GOT AWAY!")