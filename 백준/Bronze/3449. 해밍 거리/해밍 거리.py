import sys
t = int(sys.stdin.readline())
for _ in range(t):
    l = [sys.stdin.readline()[:-1] for _ in range(2)]
    c = 0
    for i in range(len(l[0])):
        if l[0][i] != l[1][i]:
            c += 1
    print(f"Hamming distance is {c}.")