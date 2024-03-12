import sys
k = int(sys.stdin.readline())
for i in range(1, k + 1):
    h = int(sys.stdin.readline())
    a = sys.stdin.readline()[:-1]
    print(f"Data Set {i}:\n{h + a.count('c') - a.count('b')}\n")