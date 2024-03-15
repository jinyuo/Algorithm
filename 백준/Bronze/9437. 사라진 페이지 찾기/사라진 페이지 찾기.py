import sys
while True:
    tmp = sys.stdin.readline()
    if tmp == "0\n":
        exit()
    n, p = map(int, tmp.split())
    tmp = (p - 1) // 2 if p % 2 == 0 else p // 2
    p_list = [tmp * 2 + 1, tmp * 2 + 2, abs(n - tmp * 2), abs(n - tmp * 2 - 1)]
    p_list.remove(p)
    p_list.sort()
    print(" ".join(str(l) for l in p_list))