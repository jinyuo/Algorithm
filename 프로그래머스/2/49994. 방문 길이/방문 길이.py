def solution(dirs):
    src = (0, 0)
    
    ways = set()
    for d in dirs:
        if d == 'U':
            dest = (src[0], src[1] + 1)
        if d == 'D':
            dest = (src[0], src[1] - 1)
        if d == 'L':
            dest = (src[0] - 1, src[1])
        if d == 'R':
            dest = (src[0] + 1, src[1])
        
        if -5 <= dest[0] <= 5 and -5 <= dest[1] <= 5:
            if (dest, src) not in ways:
                ways.add((src, dest))
            src = dest
    
    return len(ways)