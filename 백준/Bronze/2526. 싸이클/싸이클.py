N, P = map(int, input().split())
L = []
while len(L) <= 97:
    r = L[-1] if L else N
    r = r * N % P
    if r in L:
        break
    L.append(r)

print(len(L) - L.index(r))