import sys

i = 1
while True:
    L, P, V = map(int, sys.stdin.readline().strip().split(' '))
    if all(i == 0 for i in [L, P, V]):
        break

    m, r = divmod(V, P)
    print(f'Case {i}: {L * m + min(r, L)}')
    i += 1
