def solution(absolutes, signs):    
    return sum([d[1] if d[0] else -d[1] for d in zip(signs, absolutes)])