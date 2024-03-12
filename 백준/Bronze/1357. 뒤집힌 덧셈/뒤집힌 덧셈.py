import sys
def rev(n):
    return int(str(n)[::-1])


x, y = sys.stdin.readline().split()
print(rev(rev(x) + rev(y)))