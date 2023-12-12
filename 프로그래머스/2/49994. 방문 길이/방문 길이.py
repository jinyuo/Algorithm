def solution(dirs):
    src = (0, 0)
    mv_units = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

    ways = set()
    for d in dirs:
        m = mv_units[d]
        dest = (src[0] + m[0], src[1] + m[1])
        
        if -5 <= dest[0] <= 5 and -5 <= dest[1] <= 5:
            ways.add((src, dest))
            ways.add((dest, src))
            src = dest
    
    return len(ways) // 2