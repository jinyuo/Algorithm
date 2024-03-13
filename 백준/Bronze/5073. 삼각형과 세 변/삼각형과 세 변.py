import sys
for _ in sys.stdin:
    if _[:-1] == "0 0 0":
        exit()
    n = sorted(list(map(int, _.split())))
    print(["Invalid", "Scalene", "Isosceles", "Equilateral"][n.count(n[1]) if n[0] + n[1] > n[2] else 0])