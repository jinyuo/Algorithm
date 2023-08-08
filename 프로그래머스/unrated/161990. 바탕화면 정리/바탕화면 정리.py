def solution(wallpaper):   
    rows = [row.replace('.', '0').replace('#', '1') for row in wallpaper]
    cols = [''.join(row) for row in zip(*rows)]   
    row = 0
    for r in [int(row, 2) for row in rows]:
        row |= r
    row = bin(row).replace('0b', '').zfill(len(rows[0]))
    col = 0
    for c in [int(col, 2) for col in cols]:
        col |= c
    col = bin(col).replace('0b', '').zfill(len(cols[0]))    
    return [col.index('1'), row.index('1'), col.rindex('1') + 1,row.rindex('1') + 1]