def solution(park, routes):
    park = [list(p) for p in park]
    W, H = len(park[0]), len(park)
    x, y = [(i, j) for i in range(H) for j in range(W) if park[i][j] == 'S'][0]

    for r in routes:
        op, n = r.split()
        n = int(n)
        if op == 'N':
            if x - n < 0 or 'X' in [p[y] for p in park][x - n:x]:
                continue
            x -= n
        elif op == 'S':
            if x + n >= H or 'X' in [p[y] for p in park][x + 1:x + n + 1]:
                continue
            x += n
        elif op == 'W':
            if y - n < 0 or 'X' in park[x][y - n:y]:
                continue
            y -= n
        elif op == 'E':
            if y + n >= W or 'X' in park[x][y + 1:y + n + 1]:
                continue
            y += n

    return [x, y]