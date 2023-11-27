def solution(brown, yellow):
    total = brown + yellow    
    for h in range(3, int(total ** 0.5) + 1):
        w = total // h
        if w * h == total and (w - 2) * (h - 2) == yellow:
            return [w, h] 
