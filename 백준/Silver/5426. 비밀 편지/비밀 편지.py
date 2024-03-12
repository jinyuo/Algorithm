import sys
def rotate_270(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N - 1 - c][r] = m[r][c]
    return ret


n = int(sys.stdin.readline())
for _ in range(n):
    en = list(sys.stdin.readline()[:-1])
    l = int(len(en) ** 0.5)
    li = list()
    for i in range(l):
        li.append(en[l * i:l*(i+1)])

    li = rotate_270(li)
    print("".join(sum(li, [])))