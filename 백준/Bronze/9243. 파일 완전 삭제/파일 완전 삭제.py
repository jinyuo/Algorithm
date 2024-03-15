import sys
n = int(sys.stdin.readline())
f = sys.stdin.readline()[:-1]
d = sys.stdin.readline()[:-1]

if n % 2 == 0:
    print("Deletion succeeded" if f == d else "Deletion failed")
else:
    for i in range(len(f)):
        if f[i] == d[i]:
            print("Deletion failed")
            quit()
    print("Deletion succeeded")