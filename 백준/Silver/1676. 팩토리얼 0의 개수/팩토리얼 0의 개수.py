import sys
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


n = int(sys.stdin.readline())
r = str(fact(n))[::-1]
c = 0
for i in r:
    if i == "0":
        c += 1
    else:
        break
print(c)