import sys
c = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        exit()
    n1 = 3 * n
    (n2, t) = (n1 // 2, "even") if n1 % 2 == 0 else ((n1 + 1) // 2, "odd")
    n3 = 3 * n2
    n4 = n3 // 9
    print(f"{c}. {t} {n4}")
    c += 1