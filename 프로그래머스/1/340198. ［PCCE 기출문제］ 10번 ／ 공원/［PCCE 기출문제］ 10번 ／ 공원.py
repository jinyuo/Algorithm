def check(mat, width, length, park):
    if mat > width or mat > length:
        return False
    
    for j in range(0, length - mat + 1):
        for i in range(0, width - mat + 1):
            jari = [row[i:i+mat] for row in park[j:j+mat]]
            if all(l == '-1' for l in sum(jari, [])):
                return True

    return False
            
            

def solution(mats, park):
    answer = -1
    width, length = len(park[0]), len(park)
    mats = sorted(mats, reverse=True)

    for m in mats:
        if check(m, width, length, park):
            return m    
    
    return answer